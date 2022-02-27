import pytest
from fastapi import status
from httpx import AsyncClient


@pytest.mark.anyio
async def test_health_check(client: AsyncClient):
    response = await client.get("/health-check")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["version"] == "5.0.5"
