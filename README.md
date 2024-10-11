
Python 3.11


- Build sample Function
```
(exism) ➜  function git:(main) ✗ make build
PYTHONPATH=$(python -c "import sys, os.path; print(':'.join([p for p in sys.path if os.path.exists(p)]))")  \
        PYTHONHOME=$(python -c "import sys;print(sys.exec_prefix)") \
        extism-py plugin.py -o plugin.wasm
```


- Call from Python Host
```
(exism) [Proxy] ➜  host git:(main) ✗ python main.py
03e33953-f423-4d60-ba73-11148b662ae5
Schema: b'{"input": {"$schema": "https://json-schema.org/draft/2020-12/schema", "type": "object", "title": "SumParams", "properties": {"a": {"type": "integer"}, "b": {"type": "integer"}}, "required": ["a", "b"]}, "output": {"$schema": "https://json-schema.org/draft/2020-12/schema", "type": "object", "title": "SumResult", "properties": {"sum": {"type": "integer"}}, "required": ["sum"]}}'
Fetched data from https://httpbin.org/json: {'slideshow': {'author': 'Yours Truly', 'date': 'date of publication', 'slides': [{'title': 'Wake up to WonderWidgets!', 'type': 'all'}, {'items': ['Why <em>WonderWidgets</em> are great', 'Who <em>buys</em> WonderWidgets'], 'title': 'Overview', 'type': 'all'}], 'title': 'Sample Slide Show'}}
Sum Result from wasm: 3
Dumping logs 46
2024-10-11T09:31:36.938200Z TRACE extism::sdk: Call to extism_plugin_new with wasm pointer 0x7f98b0000020
2024-10-11T09:31:36.941352Z TRACE extism::manifest: Loading manifest
2024-10-11T09:31:36.953497Z TRACE extism::manifest: Manifest is JSON
2024-10-11T09:31:38.571626Z DEBUG extism::plugin: Available pages: Some(400)
2024-10-11T09:31:38.574881Z TRACE extism::timer: Extism timer created
2024-10-11T09:31:38.575089Z DEBUG extism::plugin: 03e33953-f423-4d60-ba73-11148b662ae5 created
2024-10-11T09:31:38.575178Z TRACE extism::sdk: call to extism_plugin_config with pointer 0x10d46c3b0 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.575412Z TRACE extism::sdk: calling function sum2 using extism_plugin_call plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.577137Z TRACE extism::plugin: Plugin::instance is none, instantiating plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.577144Z TRACE extism::plugin: clearing error plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.577702Z DEBUG extism::plugin: input size: 11 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.578013Z TRACE extism::current_plugin: memory_alloc(77) = 11 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.578652Z TRACE extism::timer: start event with timeout: None plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.609306Z TRACE extism::current_plugin: memory_length(100) = 32 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.609319Z TRACE extism::current_plugin: memory handle found: offs = 100, length = 32 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.609391Z  INFO extism::pdk: Summing numbers with dataclasses plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.635748Z TRACE extism::timer: handling stop event plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.635925Z DEBUG extism::plugin: output offset=144, length=378 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.635987Z TRACE extism::current_plugin: memory_length(0) = 0 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.635989Z DEBUG extism::plugin: error offset=0, length=0 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.635992Z DEBUG extism::plugin: got return code: 0 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.636057Z TRACE extism::sdk: error is NULL plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.636092Z TRACE extism::sdk: extism_plugin_output_data: offset=144, length=378 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.636308Z TRACE extism::sdk: calling function sum2 using extism_plugin_call plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.636310Z TRACE extism::plugin: clearing error plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.636312Z DEBUG extism::plugin: input size: 16 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.636315Z TRACE extism::current_plugin: memory_alloc(77) = 16 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.636331Z TRACE extism::timer: start event with timeout: None plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.636434Z TRACE extism::current_plugin: memory_length(105) = 32 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.636436Z TRACE extism::current_plugin: memory handle found: offs = 105, length = 32 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.636437Z  INFO extism::pdk: Summing numbers with dataclasses plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:38.638964Z TRACE extism::current_plugin: memory_length(149) = 24 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.836828Z TRACE extism::current_plugin: memory_alloc(185) = 292 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.837996Z TRACE extism::current_plugin: memory_length(489) = 306 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.837999Z TRACE extism::current_plugin: memory handle found: offs = 489, length = 306 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.838001Z  INFO extism::pdk: Fetched data: {"slideshow": {"author": "Yours Truly", "date": "date of publication", "slides": [{"title": "Wake up to WonderWidgets!", "type": "all"}, {"items": ["Why <em>WonderWidgets</em> are great", "Who <em>buys</em> WonderWidgets"], "title": "Overview", "type": "all"}], "title": "Sample Slide Show"}} plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.845131Z TRACE extism::current_plugin: memory_length(807) = 27 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.845136Z TRACE extism::current_plugin: memory handle found: offs = 807, length = 27 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.845138Z  INFO extism::pdk: Params: SumParams(a=1, b=2) plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.845688Z TRACE extism::timer: handling stop event plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.845691Z DEBUG extism::plugin: output offset=846, length=10 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.845694Z TRACE extism::current_plugin: memory_length(0) = 0 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.845695Z DEBUG extism::plugin: error offset=0, length=0 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.845696Z DEBUG extism::plugin: got return code: 0 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.845704Z TRACE extism::sdk: error is NULL plugin="03e33953-f423-4d60-ba73-11148b662ae5"
2024-10-11T09:31:39.845708Z TRACE extism::sdk: extism_plugin_output_data: offset=846, length=10 plugin="03e33953-f423-4d60-ba73-11148b662ae5"
```