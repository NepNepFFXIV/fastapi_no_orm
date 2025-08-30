from src.fastapi_no_orm.database import Postgres


class Repository:
    def __init__(self, postgres: Postgres):
        self.postgres = postgres

    async def select_operation(self, product_id: int):
        return

    async def insert_operation(self) -> None:
        return
