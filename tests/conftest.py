from collections.abc import AsyncGenerator, Generator
from urllib.parse import urlparse

import pytest
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient
from testcontainers.postgres import PostgresContainer

from alembic import command
from alembic.config import Config


@pytest.fixture(scope="session")
def postgres_container() -> Generator[str]:
    container = PostgresContainer("postgres:17")
    container.start()
    yield container.get_connection_url()
    container.stop()


@pytest.fixture(scope="session", autouse=True)
def patch_postgres_config(postgres_container: str) -> None:
    from src.fastapi_no_orm.settings import PostgresConfig, settings

    parsed = urlparse(postgres_container)

    settings.postgres = PostgresConfig(
        host=parsed.hostname or settings.postgres.host,
        port=parsed.port or settings.postgres.port,
        user=parsed.username or settings.postgres.user,
        password=parsed.password or settings.postgres.password,
        db_name=parsed.path.lstrip("/") or settings.postgres.db_name,
        db_schema=settings.postgres.db_schema,
    )


@pytest.fixture(scope="session", autouse=True)
def init_database_migrations(patch_postgres_config: None) -> None:
    config = Config("alembic.ini")

    command.downgrade(config, "base")
    command.upgrade(config, "head")


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient]:
    from src.fastapi_no_orm.main import create_app

    app = create_app()

    async with LifespanManager(app) as manager:
        async with AsyncClient(
            transport=ASGITransport(app=manager.app),
            base_url="http://test",
        ) as client:
            yield client
