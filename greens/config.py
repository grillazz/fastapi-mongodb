import logging
import os
from functools import lru_cache
from typing import List

from pydantic import BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    """

    BaseSettings, from Pydantic, validates the data so that when we create an instance of Settings,
    environment and testing will have types of str and bool, respectively.

    Parameters:


    Returns:
    instance of Settings

    """

    environment: str = os.getenv("ENVIRONMENT", "local")
    testing: str = os.getenv("TESTING", "0")
    up: str = os.getenv("UP", "up")
    down: str = os.getenv("DOWN", "down")
    web_server: str = os.getenv("WEB_SERVER", "web_server")
    cors_origins: List[str] = os.getenv("CORS_ORIGINS", "").split(",")

    db_url: str = os.getenv("MONGO_URL", "")
    db_name: str = os.getenv("MONGO_DB", "")
    collection_name: str = os.getenv("MONGO_COLLECTION", "")
    test_db_name: str = os.getenv("MONGO_TEST_DB", "")


@lru_cache()
def get_settings():
    log.info("Loading config settings from the environment...")
    return Settings()
