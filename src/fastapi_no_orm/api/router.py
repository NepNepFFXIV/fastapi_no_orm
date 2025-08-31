from fastapi import APIRouter

from src.fastapi_no_orm.api.service import service

router = APIRouter()


@router.get("/")
async def select_operation():
    await service.select_operation()
    return {"message": "Hello, World!"}


@router.post("/")
async def insert_operation():
    await service.insert_operation()
    return {"message": "Hello, World!"}
