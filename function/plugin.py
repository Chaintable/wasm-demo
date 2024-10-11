import json
import extism
from dataclasses import dataclass, asdict
from dc_schema import get_schema

from extism import Json
from typing import Annotated


@extism.plugin_fn
def greet():
    extism.log(extism.LogLevel.Info, "Hello, world!")
    name = extism.input_str()
    if name == "Benjamin":
        raise Exception("Sorry, we don't greet Benjamins!")
    extism.output_str(f"Hello, {name}")


@extism.plugin_fn
def sum():
    extism.log(extism.LogLevel.Info, "Summing numbers")
    extism.log(extism.LogLevel.Info, "Input: " + extism.input_str())
    extism.log(extism.LogLevel.Info, dir(extism))
    try:
        params = json.loads(extism.input_str())
        extism.log(extism.LogLevel.Info, f"Params loaded from input: {params}")
        # params = extism.input_json()
        # extism.log(extism.LogLevel.Info, f"Params: {params}")
        extism.output_json({"sum": params["a"] + params["b"]})
    except Exception as e:
        extism.log(extism.LogLevel.Error, f"Error: {e}")
    extism.log(extism.LogLevel.Info, "Summing numbers done")


@dataclass
class SumParams:
    a: int
    b: int


@dataclass
class SumResult:
    sum: int


@extism.plugin_fn
def sum_schema():
    extism.output_json(
        {"input": SumParams.json_schema(), "output": SumResult.json_schema()}
    )


@extism.import_fn("example", "get_host_info")
def get_host_info(x: str) -> str:
    pass


@extism.import_fn("example", "get_host_info2")
def get_host_info2(x: extism.JsonObject) -> str:
    pass


@extism.import_fn("example", "get_host_info3")
def get_host_info3(x: Annotated[dict, Json]) -> Annotated[dict, Json]:
    pass

@extism.import_fn("http", "fetch_json")
def fetch_json(url: str) -> str:
#def fetch_json(url: str) ->Annotated[dict, Annotated[dict, Json]]:
    pass


@extism.plugin_fn
def sum2():
    extism.log(extism.LogLevel.Info, "Summing numbers with dataclasses")
    input_str = extism.input_str()
    if input_str == "__$SCHEMA__":
        extism.output_json(
            {"input": get_schema(SumParams), "output": get_schema(SumResult)}
        )
        return

    data = fetch_json("https://httpbin.org/json")
    extism.log(extism.LogLevel.Info, f"Fetched data: {data}")

    params = SumParams(**json.loads(extism.input_str()))
    extism.log(extism.LogLevel.Info, f"Params: {params}")
    result = _sum2(params)
    extism.output_json(asdict(result))


def _sum2(params: SumParams) -> SumResult:
    return SumResult(sum=params.a + params.b)
