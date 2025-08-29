from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    yield


def create_app() -> FastAPI:
    from src.fastapi_no_orm.api.router import router

    app = FastAPI(
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
    )

    app.include_router(router)

    return app


app = create_app()
