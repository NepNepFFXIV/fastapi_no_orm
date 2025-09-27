from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status

from src.fastapi_no_orm.api.dependency import get_service
from src.fastapi_no_orm.api.schemas import NewOperationRequest, OperationResponse
from src.fastapi_no_orm.api.service import Service

router = APIRouter()


@router.get("/", response_model=OperationResponse)
async def select_operation(service: Service = Depends(get_service)) -> Any:
    operation = await service.select_operation()
    if operation:
        return OperationResponse.from_Operation(operation)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Operation not found",
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
async def insert_operation(
    request_body: NewOperationRequest,
    service: Service = Depends(get_service),
) -> Any:
    await service.insert_operation(request_body.description)
