import pytest
from fastapi import status
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_root(client: AsyncClient):
    response = await client.get("/health-check")
    assert response.status_code == status.HTTP_200_OK
