from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app_name.routers import router as v1
from app_name import config
from app_name.utils import get_logger, init_mongo

global_settings = config.get_settings()

if global_settings.environment == "local":
    get_logger("uvicorn")

app = FastAPI()

app.include_router(v1, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    app.state.logger = get_logger(__name__)
    app.state.logger.info(f"Starting app_name...")
    app.mongodb_client = await init_mongo(global_settings.db_url)
    app.database = app.mongodb_client[global_settings.db_name]


@app.get("/", include_in_schema=False)
def get_swagger():
    return RedirectResponse(url="/docs")


@app.on_event("shutdown")
async def shutdown_event():
    app.state.logger.info(f"Stoping app_name...")
    app.mongodb_client.close()


@app.get("/health-check")
async def health_check():
    return {"status": "ok"}
