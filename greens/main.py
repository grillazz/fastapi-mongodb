from fastapi import FastAPI

from greens import config
from greens.routers import router as v1
from greens.utils import get_logger, init_mongo

global_settings = config.get_settings()

if global_settings.environment == "local":
    get_logger("uvicorn")


app = FastAPI()

app.include_router(v1, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    app.state.logger = get_logger(__name__)
    app.state.logger.info("Starting greens on your farmland...")
    app.state.mongo_client, app.state.mongo_database, app.state.mongo = await init_mongo(
        global_settings.db_name, global_settings.db_url, global_settings.collection
    )


@app.on_event("shutdown")
async def shutdown_event():
    app.state.logger.info("Parking tractors in garage...")


@app.get("/health-check")
async def health_check():
    # TODO: check settings dependencies passing as args and kwargs
    # stuff = await database.add_stuff()
    a = 5
    try:
        assert 5 / 0
    except Exception:
        app.state.logger.exception("My way or highway...")
