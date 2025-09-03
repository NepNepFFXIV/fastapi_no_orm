from typing import Self

from pydantic import BaseModel

from src.fastapi_no_orm.api.models import Operation


class NewOperationRequest(BaseModel):
    description: str


class OperationResponse(BaseModel):
    operation_id: int
    description: str

    @classmethod
    def from_Operation(cls, operation: Operation) -> Self:
        return cls(operation_id=operation.id, description=operation.description)
