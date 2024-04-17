from contextlib import asynccontextmanager

from fastapi import FastAPI

from greens.config import settings as global_settings
from greens.routers import router as v1
from greens.services.repository import get_mongo_meta
from greens.utils import get_logger, init_mongo

if global_settings.environment == "local":
    get_logger("uvicorn")


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.logger = get_logger(__name__)
    app.state.logger.info("Starting greens on your farmland...mmm")
    app.state.mongo_client, app.state.mongo_db, app.state.mongo_collection = (
        await init_mongo(
            global_settings.mongodb_database,
            global_settings.mongodb_url.unicode_string(),
            global_settings.mongodb_collection,
        )
    )
    try:
        yield
    finally:
        app.state.logger.info("Parking tractors in garage...")


app = FastAPI(lifespan=lifespan, title="Greens API", version="0.5.0")

app.include_router(v1, prefix="/api/v1")


@app.get("/health-check")
async def health_check():
    # # TODO: check settings dependencies passing as args and kwargs
    # a = 5
    # try:
    #     assert 5 / 0
    # except Exception:
    #     app.state.logger.exception("My way or highway...")
    return await get_mongo_meta()
