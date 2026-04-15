# time

With basic python `time` module, you can measure the execution time of your
code. This is a very simple way to do profiling, but it can be useful to quickly
check the performance of your code, specially if you want to check the
performance of a specific function or a block of code.

## Installation

No need, `time` module is part of the Python standard library, so you can use it
without installing anything.

## Basic usage

To measure the execution time of a function, you can use the `time` module with
`perf_counter` and `process_time` functions. The first one measures the wall
clock time, while the second one measures the CPU time.

To execute this example, you can run the script with `python` command:

```bash
python -m basic_usage.main
```

## Complex usage

For more complex usage, you can use the `timeit` module, which provides a simple
way to time small bits of Python code. This module allows to execute the code
multiple times and get the average execution time, which can be useful to get
more accurate results.

To execute this example, you can run the script with `python` command:

```bash
python -m complex_usage.main
```
