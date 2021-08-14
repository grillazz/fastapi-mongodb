import logging
import os
from functools import lru_cache

from pydantic import BaseSettings
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")


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

    db_url: str = os.getenv("MONGO_URL", "")
    db_name: str = os.getenv("MONGO_DB", "")
    collection: str = os.getenv("MONGO_COLLECTION", "")
    test_db_name: str = os.getenv("MONGO_TEST_DB", "")


@lru_cache()
def get_settings():
    log.info("FARM message: Loading config settings from the environment...")
    return Settings()
