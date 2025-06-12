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

To see the results, you can run:

```bash
uv run python -m line_profiler output/basic_usage.lprof
```
