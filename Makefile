install:
	uv sync

py-utils:
	uv run py-utils

build:
	uv build

test:
	uv run pytest -vv

lint:
	uv run ruff check --fix

