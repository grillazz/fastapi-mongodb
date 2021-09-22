from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from greens import config
from greens.routers.api import router as v1
from greens.utils import get_logger

logger = get_logger(__name__)
global_settings = config.get_settings()

app = FastAPI()

app.include_router(v1, prefix="/api/v1")


async def init_mongo() -> AsyncIOMotorClient:
    mongo_client = AsyncIOMotorClient(global_settings.db_url)
    mongo_database = mongo_client[global_settings.db_name]
    mongo_collections = {
        global_settings.collection: mongo_database.get_collection(global_settings.collection),
    }
    return mongo_client, mongo_database, mongo_collections


@app.on_event("startup")
async def startup_event():
    logger.info("Starting greens on your farmland...")
    app.state.mongo_client, app.state.mongo_database, app.state.mongo = await init_mongo()
    app.logger = logger


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Parking tractors in garage...")


@app.get("/health-check")
async def health_check():
    # TODO: check settings dependencies passing as args and kwargs
    # stuff = await database.add_stuff()
    a = 5
    try:
        assert 5 / 0
    except Exception:
        logger.exception("My way or highway...")
