
from fastapi import APIRouter

from greens import config
from greens.routers.exceptions import NotFoundHTTPException
from greens.schemas.vegs import DocumentResponse, ObjectIdField
from greens.services.repository import get_document


global_settings = config.get_settings()
collection = global_settings.collection

router = APIRouter()


@router.get(
    "/{object_id}",
    response_description="Document retrieved",
    response_model=DocumentResponse,
)
async def get_ro_document(object_id: ObjectIdField):
    try:
        document = await get_document(object_id, collection)
    except ValueError:
        raise NotFoundHTTPException(f"No document found for {object_id=} in {collection=}")
    return document



    # try:
    #     assert 5 / 0
    # except Exception:
    #     logger.exception("My way or highway...")