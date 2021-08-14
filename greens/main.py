import logging

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from greens import config

log = logging.getLogger("uvicorn")
global_settings = config.get_settings()

app = FastAPI()


async def init_mongo() -> AsyncIOMotorClient:
    mongo_client = AsyncIOMotorClient(global_settings.db_url)
    mongo_database = mongo_client[global_settings.db_name]
    mongo_collections = {
        global_settings.collection: mongo_database.get_collection(global_settings.collection),
    }
    return mongo_client, mongo_database, mongo_collections


@app.on_event("startup")
async def startup_event():
    log.info("FARM message: Starting greens on your farmland...")
    app.state.mongo_client, app.state.mongo_database, app.state.mongo = await init_mongo()


@app.on_event("shutdown")
async def shutdown_event():
    log.info("FARM message: Shutting down - your tractors were parked in garage...")


# @app.get("/health-check")
# async def health_check():
#     # TODO: check settings dependencies passing as args and kwargs
#     stuff = await database.add_stuff()
#     return stuff
