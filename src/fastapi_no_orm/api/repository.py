from src.fastapi_no_orm.database import Postgres


class Repository:
    def __init__(self, postgres: Postgres):
        self.postgres = postgres

    async def select_operation(self, product_id: int):
        query = """
            select
                id,
                description
            from no_orm.operation
            where id = $1
        """
        async with self.postgres.get_connection() as connection:
            return await connection.fetchrow(query, product_id)

    async def insert_operation(self) -> None:
        return
