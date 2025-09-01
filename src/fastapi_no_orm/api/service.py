from random import randint

from src.fastapi_no_orm.api.models import Operation
from src.fastapi_no_orm.api.repository import Repository
from src.fastapi_no_orm.database import postgres


class Service:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def select_operation(self) -> Operation | None:
        product_id = randint(1, 1000)
        return await self.repository.select_operation(product_id)

    async def insert_operation(self, description: str):
        await self.repository.insert_operation(description)


repository = Repository(postgres)
service = Service(repository)
