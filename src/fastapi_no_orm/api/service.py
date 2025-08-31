from src.fastapi_no_orm.api.repository import Repository
from src.fastapi_no_orm.database import postgres


class Service:
    def __init__(self, repository: Repository):
        self.repository = repository


repository = Repository(postgres)
service = Service(repository)
