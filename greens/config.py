import os

from pydantic import MongoDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Represents the configuration settings for the application.

    Args:
        environment (str): The environment in which the application is running. Defaults to "local".
        testing (str): The testing mode of the application. Defaults to "0".
        up (str): The up status of the application. Defaults to "up".
        down (str): The down status of the application. Defaults to "down".
        web_server (str): The web server used by the application. Defaults to "web_server".
        db_url (str): The URL of the MongoDB database.
        db_name (str): The name of the MongoDB database.
        collection (str): The name of the MongoDB collection.
        test_db_name (str): The name of the MongoDB test database.

    """
    environment: str = os.getenv("ENVIRONMENT", "local")
    testing: str = os.getenv("TESTING", "0")
    up: str = os.getenv("UP", "up")
    down: str = os.getenv("DOWN", "down")
    web_server: str = os.getenv("WEB_SERVER", "web_server")

    db_url: str = os.getenv("MONGO_URL", "")
    mongodb_database: str = os.getenv("MONGODB_DATABASE", "")
    collection: str = os.getenv("MONGODB_COLLECTION", "")
    mongodb_test: str = os.getenv("MONGODB_TEST", "")

    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_USER: str
    MONGODB_PASSWORD: str

    @computed_field
    @property
    def mongodb_url(self) -> MongoDsn:

        return MultiHostUrl.build(
            scheme="mongodb",
            host=self.MONGODB_HOST,
            port=self.MONGODB_PORT,
            username=self.MONGODB_USER,
            password=self.MONGODB_PASSWORD,

            path=self.mongodb_name, # TODO: url query params goes here
        )

settings = Settings()
