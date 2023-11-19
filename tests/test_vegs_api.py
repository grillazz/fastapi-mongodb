import pytest
# from bson import ObjectId
from fastapi import status
from httpx import AsyncClient

pytestmark = pytest.mark.anyio


@pytest.mark.parametrize(
    "payload, status_code",
    (
        (
            {"name": "Corn", "desc": "Corn on the cob"},
            status.HTTP_201_CREATED,
        ),
    ),
)
# Test document create endpoint
async def test_add_document(client: AsyncClient, payload: dict, status_code: int):
    # Send POST request
    response = await client.post("/api/v1/vegs", json=payload)
    # Assert HTTP code and if received document id is valid
    assert response.status_code == status_code
    # assert ObjectId.is_valid(response.json()["id"])
