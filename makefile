.PHONY: run
run:
	uv run fastapi dev src/fastapi_no_orm/main.py

.PHONY: ruff
ruff:
	uv run ruff check --fix
	uv run ruff format
