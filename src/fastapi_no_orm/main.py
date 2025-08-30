from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.fastapi_no_orm.database import postgres
from src.fastapi_no_orm.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    await postgres.connect(settings.postgres.postgres_url)
    yield
    await postgres.close()


def create_app() -> FastAPI:
    from src.fastapi_no_orm.api.router import router

    app = FastAPI(
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
    )

    app.include_router(router)

    return app


app = create_app()
