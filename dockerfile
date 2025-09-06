FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS builder

ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev

COPY ./uv.lock ./pyproject.toml ./.python-version /app/
COPY ./src /app/src

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

FROM python:3.13-slim-bookworm

WORKDIR /app

COPY --from=builder /app /app

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH="/app"

EXPOSE 8000

CMD uvicorn src.fastapi_no_orm.main:app --host 0.0.0.0 --port 8000 --no-access-log
