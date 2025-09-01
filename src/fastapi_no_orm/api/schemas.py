from pydantic import BaseModel


class NewOperationRequest(BaseModel):
    description: str
