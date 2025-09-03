from typing import Any

from pydantic import BaseModel

from src.fastapi_no_orm.api.models import Operation


class NewOperationRequest(BaseModel):
    description: str


class OperationResponse(BaseModel):
    operation_id: int
    description: str

    @staticmethod
    def from_Operation(operation: Operation) -> dict[str, Any]:
        return {
            "operation_id": operation.id,
            "description": operation.description,
        }
