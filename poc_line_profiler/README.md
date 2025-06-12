# line_profiler

[line_profile](https://github.com/pyutils/line_profiler) is a Python module to
perform line-by-line profiling of your Python application.

## Installation

As manage package dependencies, we will use `uv`, as it is a lightweight
alternative to `poetry`. Very simple to use, just run `uv init` to create a
`pyproject.toml` file, and then you can add dependencies to it. For example, to add
`line_profiler`, you can run:

```bash
uv add line_profiler
```

## Basic usage

To quickly have an example running, I decided to copy/paste
[online example available here](https://kernprof.readthedocs.io/en/latest/#line-profiler-basic-usage).

To execute the command with profiling, you can run:

```bash
uv run kernprof -l -v -o ./output/basic_usage.lprof basic_usage/main.py
```

> IMPORTANT: line_profiler requires the `-l` flag to enable line-by-line profiling,
> and the `-v` flag to display the results in the console.

We can customize Time unit. By default, `line_profile` uses microseconds (1e-6
seconds), but by adding option `--unit 1e-3`, Time unit is set to milliseconds
(1e-3 seconds).

```bash
uv run kernprof -l -v --unit 1e-0 -o ./output/basic_usage.lprof basic_usage/main.py
```

To see the results, you can run:

```bash
uv run python -m line_profiler output/basic_usage.lprof --unit 1e-3
```

## Custom implementation

As my custom example, I'd like to include `line_profiler` into a FastAPI
application.

Add `fastapi` as a dependency to your project:

```bash
uv add "fastapi[standard]"
```

And to run the FastAPI application with kernprof:

```bash
poetry run kernprof -l -v -o ./output/custom_usage.lprof custom_usage/main.py
```

Execute some curls to register/get some data. Profiling is implemented in
`InMemory.retrieve` and `InMemory.store` methods. Both methods include delays to
simulate slow operations.

```bash
curl --request POST http://127.0.0.1:8000/data -d '{"key": "hello", "value": "world"}' -H "Content-Type: application/json"
curl --request GET http://127.0.0.1:8000/data -d '{"key": "hello"}' -H "Content-Type: application/json"
curl --request POST http://127.0.0.1:8000/data -d '{"key": "slow_hello", "value": "world"}' -H "Content-Type: application/json"
curl --request GET http://127.0.0.1:8000/data -d '{"key": "slow_hello"}' -H "Content-Type: application/json"
```

To see the results, you can run:

```bash
uv run python -m line_profiler output/custom_usage.lprof --unit 1e-3
```
