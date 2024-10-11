build:
	PYTHONPATH=$$(python -c "import sys, os.path; print(':'.join([p for p in sys.path if os.path.exists(p)]))")  \
	PYTHONHOME=$$(python -c "import sys;print(sys.exec_prefix)") \
	extism-py plugin.py -o plugin.wasm

run:
	extism call plugin.wasm sum --input='{"a": 20, "b": 21}' --wasi --log-level=debug
	extism call plugin.wasm greet --input=Benjamin --wasi --log-level=debug
