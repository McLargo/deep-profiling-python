# py-spy

[py-spy](https://github.com/benfred/py-spy) is a sampling profiler for Python
code. That means, in difference to deterministic profiles, it gets samples of
the stack trace at regular intervals. On each interval, it checks with functions
are currently being executed. The more often a function appears in the samples,
the more time it is taking in the execution of the program.

It has the advantage that can be use in production environments as it adds very
low overhead on top of the program execution. Additionally, no code changes are
required to start profiling with py-spy.

## Installation

As manage package dependencies, we will use `uv`, as it is a lightweight
alternative to `poetry`. Very simple to use, just run `uv init` to create a
`pyproject.toml` file, and then you can add dependencies to it. For example, to
add `py-spy`, you can run:

```bash
uv add py-spy
```

## Basic usage

`py-spy` can be used in different ways, but the most common one is to use it in `top` mode, which shows a live view of the most expensive functions in your code. To use it, you need to know the PID of the process you want to profile.

To execute the expensive cpu intensive task, you can run the `main.py` file in
this directory. It will print the PID of the process, and you can use that PID
to attach `py-spy` to it.

```bash
uv run python -m main
```

Then, in another terminal, you can run the command printed by the `main.py`
script to attach `py-spy` to the process:

```bash
uv run py-spy top --pid <pid>
```

### Troubleshooting

In case you are required to use `sudo` to run the `py-spy` command, you can use
`env` to preserve the environment variables and avoid having to specify the full
path to `py-spy`:

```bash
sudo env "PATH=$PATH" uv run py-spy top --pid <PID>
```
