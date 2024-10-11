# run this using `poetry run python example.py`!
import sys

import json
import hashlib
import pathlib
import httpx
from typing import Dict

import extism
from extism import Function, host_fn, ValType, Plugin, set_log_custom, Json
from typing import Annotated


@host_fn(name="get_host_info", namespace="example")
def get_host_info() -> str:
    return "Host info"


@host_fn(name="get_host_info2", namespace="example")
def get_host_info2(d: Annotated[dict, Json]) -> str:
    print(d)
    return "Host info 2"


@host_fn(name="get_host_info3", namespace="example")
def get_host_info3(d: Annotated[dict, Json]) -> Annotated[dict, Json]:
    print(d)
    return {"result": "Host info 3"}


# 添加新的函数定义
@host_fn(name="get_host_info", namespace="example")
def get_host_info_with_param(x: str) -> str:
    return f"Host info: {x}"

@host_fn(name="fetch_json", namespace="http")
#def fetch_json(url: str) -> Annotated[dict, Json]:
def fetch_json(url: str) -> str:
    try:
        response = httpx.get(url, timeout=10)  # 添加超时
        response.raise_for_status()  # 检查HTTP错误
        data = response.json()
        print(f"Fetched data from {url}: {data}")
        return json.dumps(data)
    except httpx.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return json.dumps({"error": str(e)})
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return json.dumps({"error": "Invalid JSON response"})
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return json.dumps({"error": str(e)})

def main():
    logs = []
    logBuffer = set_log_custom(lambda s: logs.append(s.strip()), "trace")
    wasm_file_path = pathlib.Path(__file__).parent.parent / "function" / "plugin.wasm"
    wasm = wasm_file_path.read_bytes()
    hash = hashlib.sha256(wasm).hexdigest()
    # https://extism.org/docs/concepts/manifest
    # https://raw.githubusercontent.com/extism/extism/main/manifest/schema.json
    manifest = {
        "wasm": [
            {"data": wasm, "hash": hash},
        ],
        "memory": {
            # The max amount of pages the plugin can allocate
            # One page is 64Kib. e.g. 16 pages would require 1MiB.
            "max_pages": 400,
            # The max size of an Extism HTTP response in bytes
            "max_http_response_bytes": 4096,
            # The max size of all Extism vars in bytes
            "max_var_bytes": 4096,
        },
        # An optional set of hosts this plugin can communicate with.
        # This only has an effect if the plugin makes HTTP requests.
        # Note: if left empty then no hosts are allowed and if `null` then all hosts are allowed.
        "allowed_hosts": [
            "example.com",
            "extism.org",
        ],
        # An optional set of mappings between the host's filesystem and the paths a plugin can access.
        # This only has an effect if the plugin is provided with WASI capabilities.
        # Note: if left empty or `null`, then no file access is granted.
        "allowed_paths": {
            ".": "plugin/path",
        },
        # The "config" key is a free-form map that can be passed to the plugin.
        # A plugin author must know the arbitrary data this map may contain, so your own documentation should include some information about the "config" passed in.
        "config": {"mykey": "myvalue"},
    }

    with Plugin(
        manifest,
        wasi=True,
        config={
            "allowed_hosts": ["example.com"],
            "allowed_urls": ["*"],
        },
        functions=[
            get_host_info,
            get_host_info2,
            get_host_info_with_param,
            get_host_info3,
            fetch_json,
        ],
    ) as plugin:
        print(plugin.id)

        # Get schema
        schema = plugin.call("sum2", "__$SCHEMA__")
        print(f"Schema: {schema}")

        # Call `sum2`
        result = plugin.call("sum2", json.dumps({"a": 1, "b": 2}))
        j = json.loads(result)
        print(f"Sum Result from wasm: {j['sum']}")

    # Drain logs and print
    logBuffer.drain()
    print("Dumping logs", len(logs))
    for line in logs:
        print(line)


if __name__ == "__main__":
    main()
