from decouple import config
from functools import lru_cache

from pydantic import BaseSettings

from app_name.utils import get_logger

logger = get_logger(__name__)


class Settings(BaseSettings):
    """

    BaseSettings, from Pydantic, validates the data so that when we create an instance of Settings,
    environment and testing will have types of str and bool, respectively.

    Parameters:


    Returns:
    instance of Settings

    """

    environment: str = config("ENVIRONMENT", default="local")
    testing: str = config("TESTING", default="0")
    up: str = config("UP", default="up")
    down: str = config("DOWN", default="down")
    web_server: str = config("WEB_SERVER", default="web_server")

    db_url: str = config("MONGO_URL", default="")
    db_name: str = config("MONGO_DB", default="")
    collection: str = config("MONGO_COLLECTION", default="")
    test_db_name: str = config("MONGO_TEST_DB", default="")


@lru_cache
def get_settings():
    logger.info("Loading config settings from the environment...")
    return Settings()
