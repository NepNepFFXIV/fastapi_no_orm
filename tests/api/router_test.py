import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.anyio


async def test_select_operation(client: AsyncClient) -> None:
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json()["operation_id"] is not None
    assert response.json()["description"] is not None


async def test_insert_operation(client: AsyncClient) -> None:
    response = await client.post("/", json={"description": "test"})
    assert response.status_code == 201
