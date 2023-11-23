from bson import ObjectId
from pymongo.errors import WriteError
from pymongo.results import InsertOneResult

import greens.main as greens
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
    if document := await greens.app.state.mongo_collection[collection].find_one(document_filter):
        return await document_id_helper(document)
    else:
        raise ValueError(f"No document found for {document_id=} in {collection=}")


async def create_document(document, collection: str) -> InsertOneResult:
    """

    :param document:
    :param collection:
    :return:
    """
    try:
        document: InsertOneResult = await greens.app.state.mongo_collection[collection].insert_one(document.model_dump())
        return document
    except WriteError as e:
        # TODO: this not make sense as id from mongo will be always unique if we not pass it
        raise AlreadyExistsHTTPException(msg=str(e)) from e

async def get_mongo_meta() -> dict:
    list_databases = await greens.app.state.mongo_client.list_database_names()
    list_of_collections = {}
    for db in list_databases:
        list_of_collections[db] = await greens.app.state.mongo_client[db].list_collection_names()
    mongo_meta = await greens.app.state.mongo_client.server_info()
    return {"version": mongo_meta["version"], "databases": list_databases, "collections": list_of_collections}
