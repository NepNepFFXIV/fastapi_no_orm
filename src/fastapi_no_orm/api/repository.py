from src.fastapi_no_orm.database import Postgres


class Repository:
    def __init__(self, postgres: Postgres):
        self.postgres = postgres
