# cProfile

[cProfile](https://docs.python.org/3/library/profile.html) is a built-in Python
module to perform deterministic profiling of your Python application. It
provides a way to measure the time spent in each function and the number of
calls made to each function.

## Installation

As `cProfile` is a built-in module, there is no need to install it. You can
directly import it in your Python code and use it for profiling.

## Basic usage

In my basic example, I will use `cProfile` to profile a simple Python script
that reads a file, and for each line, it does a call to 3pp and save the the
result in a database (both 3pp and database are mocked).

To execute the command with profiling, displaying results in the console, you
can run:

```bash
python -m basic_usage.main --profile-screen
```

See a brief explanation of the most relevant columns:

- `ncalls`: number of calls to the function
- `tottime`: total time spent in the function, excluding time spent in calls to
  sub-functions.
- `percall`: time spent in the function per call, excluding time spent in calls  to sub-functions. It is calculated as `tottime / ncalls`.
- `cumtime`: cumulative time spent in the function, including time spent in
  calls to sub-functions.
- `percall`: time spent in the function per call, including time spent in calls to sub-functions. It is calculated as `cumtime / ncalls`.
- `filename:lineno(function)`: the file name, line number, and function name
  where the function is defined.

### Viewing results in a GUI

To view the result in a GUI, you can use `snakeviz` (remember to install it
first with `uv add snakeviz`), which is a browser-based viewer for Python
profiling data. First, we need to save the profiling results to a file. We can
do this by running the following command:

```bash
python -m cProfile -o basic_usage/output.prof basic_usage/main.py
uv run snakeviz basic_usage/output.prof
```

It will open a new tab in your browser with a visual display of the profiling
results, allowing you to explore the call graph and identify performance
bottlenecks in your code.
