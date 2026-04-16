# profyle

[profyle](https://github.com/vpcarlos/profyle) is a python library that provides
a simple and efficient way to profile your API python application. Supports main
frameworks like FastAPI, Flask and Django.

## Installation

As manage package dependencies, we will use `uv`, as it is a lightweight
alternative to `poetry`. Very simple to use, just run `uv init` to create a
`pyproject.toml` file, and then you can add dependencies to it. For example, to
add `profyle`, you can run:

```bash
uv add profyle
```

## API usage

To quickly have an example running, I decided to copy/paste example available on
github for FastAPI framework.

To run the FastAPI application with profyle, you can run:

```bash
uv run uvicorn main:app --reload
uv run profyle start
```

Both those commands start the application and the profyle dashboard. As soon as
you start hitting endpoints in your API, you will see the traces appearing in
the dashboard.

## Final word

Library is quite interesting, but is not actively maintained. Documentation is
not working as expected, and I even need to do some tweaks to make it work in
the library itself (a problem with Jinja2).
