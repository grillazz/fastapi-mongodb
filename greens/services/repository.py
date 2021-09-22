from bson import ObjectId
from greens import main as greens


async def get_document(document_id: str, collection: str) -> dict:
    """Retrieve document from collection for ObjectId

    Args:
        document_id:
        collection:

    Returns:

    Raises:
        ValueError: if document for ObjectId not exists in collection
    """
    document_filter = {"_id": ObjectId(document_id)}
    if document := await greens.app.state.mongo[collection].find_one(document_filter):
        # return research_object_helper(research_object)
        return document
    else:
        raise ValueError(f"No document found for {document_id=} in {collection=}")