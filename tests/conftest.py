from collections.abc import AsyncGenerator

import pytest
from httpx import AsyncClient, ASGITransport

from greens.config import settings as global_settings
from greens.main import app, init_mongo
from greens.utils import get_logger


@pytest.fixture(
    params=[
        pytest.param(("asyncio", {"use_uvloop": True}), id="asyncio+uvloop"),
    ]
)
def anyio_backend(request):
    return request.param


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient]:
    transport = ASGITransport(
        app=app,
    )
    async with AsyncClient(
        base_url="http://testserver",
        transport=transport,
    ) as client:
        app.state.logger = get_logger(__name__)
        app.state.mongo_client, app.state.mongo_db, app.state.mongo_collection = await init_mongo(
            global_settings.mongodb_test,
            global_settings.mongodb_url.unicode_string(),
            global_settings.mongodb_collection,
        )
        yield client
