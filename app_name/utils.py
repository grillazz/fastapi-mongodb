import logging
from functools import lru_cache

from pymongo import MongoClient
from rich.console import Console
from rich.logging import RichHandler

console = Console(color_system="256", width=150, style="blue")


@lru_cache
def get_logger(module_name):
    """

    Args:
        module_name:

    Returns:

    """
    logger = logging.getLogger(module_name)
    handler = RichHandler(
        rich_tracebacks=True, console=console, tracebacks_show_locals=True
    )
    handler.setFormatter(
        logging.Formatter(
            "%(name)s - [ %(threadName)s:%(funcName)s:%(lineno)d ] - %(message)s"
        )
    )
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


async def init_mongo(db_url: str):
    """

    Args:
        db_url:

    Returns:

    """
    return MongoClient(db_url)
