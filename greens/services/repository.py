from bson import ObjectId
from pymongo.errors import WriteError

from greens import main as greens
from greens.routers.exceptions import AlreadyExistsHTTPException


async def document_id_helper(document: dict) -> dict:
    document["id"] = document.pop("_id")
    return document


async def retrieve_document(document_id: str, collection: str) -> dict:
    """

    :param document_id:
    :param collection:
    :return:
    """
    document_filter = {"_id": ObjectId(document_id)}
    if document := await greens.app.state.mongo[collection].find_one(document_filter):
        return await document_id_helper(document)
    else:
        raise ValueError(f"No document found for {document_id=} in {collection=}")


async def create_document(document: dict, collection: str) -> dict:
    """

    :param document:
    :param collection:
    :return:
    """
    try:
        document = await greens.app.state.mongo[collection].insert_one(document)
        return await retrieve_document(document.inserted_id, collection)
    except WriteError:
        raise AlreadyExistsHTTPException(f"Document with {document.inserted_id=} already exists")
