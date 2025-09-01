from src.fastapi_no_orm.api.models import Operation
from src.fastapi_no_orm.database import Postgres


class Repository:
    def __init__(self, postgres: Postgres):
        self.postgres = postgres

    async def select_operation(self, product_id: int) -> Operation | None:
        query = """
            select
                id,
                description
            from no_orm.operation
            where id = $1
        """
        async with self.postgres.get_connection() as connection:
            result = await connection.fetchrow(query, product_id)
            if result:
                return Operation(**result)
            return None

    async def insert_operation(self, description: str) -> None:
        query = """
            insert into no_orm.operation (description) values ($1)
        """
        async with self.postgres.get_connection() as connection:
            await connection.execute(query, description)
