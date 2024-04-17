import os

from pydantic import MongoDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for the application"""

    environment: str = os.getenv("ENVIRONMENT", "local")
    testing: str = os.getenv("TESTING", "0")
    up: str = os.getenv("UP", "up")
    down: str = os.getenv("DOWN", "down")
    web_server: str = os.getenv("WEB_SERVER", "web_server")

    mongodb_database: str = os.getenv("MONGODB_DATABASE", "")
    mongodb_collection: str = os.getenv("MONGODB_COLLECTION", "")
    mongodb_test: str = os.getenv("MONGODB_TEST", "")

    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_USER: str
    MONGODB_PASSWORD: str
    MONGODB_PARAMS: str

    @computed_field
    @property
    def mongodb_url(self) -> MongoDsn:
        return MultiHostUrl.build(
            scheme="mongodb",
            host=self.MONGODB_HOST,
            port=self.MONGODB_PORT,
            username=self.MONGODB_USER,
            password=self.MONGODB_PASSWORD,
            path=self.MONGODB_PARAMS,
        )


settings = Settings()
