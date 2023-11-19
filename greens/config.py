import os

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
    db_name: str = os.getenv("MONGO_DB", "")
    collection: str = os.getenv("MONGO_COLLECTION", "")
    test_db_name: str = os.getenv("MONGO_TEST_DB", "")


settings = Settings()
