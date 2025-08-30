from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Final

import asyncpg

DB_NOT_CONNECTED_MSG: Final[str] = "Database is not connected"


class Postgres:
    __slots__ = ("_pool",)

    def __init__(self) -> None:
        self._pool: asyncpg.Pool | None = None

    async def connect(self, database_url: str) -> None:
        if self._pool is not None:
            raise RuntimeError(DB_NOT_CONNECTED_MSG)

        self._pool = await asyncpg.create_pool(database_url)

    async def close(self) -> None:
        if self._pool is None:
            raise RuntimeError(DB_NOT_CONNECTED_MSG)

        await self._pool.close()
        self._pool = None

    @asynccontextmanager
    async def get_connection(self) -> AsyncGenerator[asyncpg.Connection]:
        if self._pool is None:
            raise RuntimeError(DB_NOT_CONNECTED_MSG)

        async with self._pool.acquire() as connection:
            yield connection

    @asynccontextmanager
    async def get_transaction(self) -> AsyncGenerator[asyncpg.Connection]:
        if self._pool is None:
            raise RuntimeError(DB_NOT_CONNECTED_MSG)

        async with self._pool.acquire() as connection:
            async with connection.transaction():
                yield connection


postgres: Postgres = Postgres()
