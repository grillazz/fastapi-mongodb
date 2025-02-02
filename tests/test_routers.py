import pytest
from fastapi import status
from httpx import AsyncClient
from inline_snapshot import snapshot


@pytest.mark.anyio
async def test_health_check(client: AsyncClient):
    response = await client.get("/health-check")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == snapshot(
        {
            "version": "7.0.8",
            "databases": ["admin", "config", "local"],
            "collections": {
                "admin": ["system.version", "system.users"],
                "config": ["system.sessions"],
                "local": ["startup_log"],
            },
        }
    )
