from typing import Any

from fastapi import APIRouter, HTTPException, status

from src.fastapi_no_orm.api.schemas import NewOperationRequest, OperationResponse
from src.fastapi_no_orm.api.service import service

router = APIRouter()


@router.get("/")
async def select_operation() -> OperationResponse:
    operation = await service.select_operation()
    if operation:
        return OperationResponse.from_Operation(operation)
    raise HTTPException(status_code=404, detail="Operation not found")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def insert_operation(request_body: NewOperationRequest) -> Any:
    await service.insert_operation(request_body.description)
