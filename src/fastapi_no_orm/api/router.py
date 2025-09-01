from fastapi import APIRouter

from src.fastapi_no_orm.api.schemas import NewOperationRequest
from src.fastapi_no_orm.api.service import service

router = APIRouter()


@router.get("/")
async def select_operation():
    return await service.select_operation()


@router.post("/")
async def insert_operation(request_body: NewOperationRequest):
    await service.insert_operation(request_body.description)
    return {"message": "Success!"}
