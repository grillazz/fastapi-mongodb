from typing import AsyncGenerator

import pytest
from httpx import AsyncClient

from greens import config
from greens.main import app, init_mongo
from greens.utils import get_logger

global_settings = config.get_settings()


@pytest.fixture(
    params=[
        pytest.param(("asyncio", {"use_uvloop": True}), id="asyncio+uvloop"),
    ]
)
def anyio_backend(request):
    return request.param


@pytest.fixture
async def client() -> AsyncGenerator:
    async with AsyncClient(
        app=app,
        base_url="http://testserver",
    ) as client:
        app.state.logger = get_logger(__name__)
        app.state.mongo = await init_mongo(
            global_settings.test_db_name, global_settings.db_url, global_settings.collection
        )
        yield client
