from functools import cache

from fastapi import Depends

from src.fastapi_no_orm.api.repository import Repository
from src.fastapi_no_orm.api.service import Service
from src.fastapi_no_orm.database import postgres


@cache
def get_repository() -> Repository:
    return Repository(postgres)


@cache
def get_service(repository: Repository = Depends(get_repository)) -> Service:
    return Service(repository)
