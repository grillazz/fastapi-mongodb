from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_201_CREATED

from greens.config import settings as global_settings
from greens.routers.exceptions import NotFoundHTTPException
from greens.schemas.vegs import Document, DocumentResponse, ObjectIdField
from greens.services.repository import create_document, retrieve_document

collection = global_settings.collection

router = APIRouter()


@router.post(
    "",
    status_code=HTTP_201_CREATED,
    response_description="Document created",
    response_model=DocumentResponse,
)
async def add_document(payload: Document):
    """

    :param payload:
    :return:
    """
    try:
        # payload = jsonable_encoder(payload)
        document = await create_document(payload, collection)
        return {"id": str(document.inserted_id)}
    except ValueError as exception:
        raise NotFoundHTTPException(msg=str(exception)) from exception


@router.get(
    "/{object_id}",
    response_description="Document retrieved",
    response_model=DocumentResponse,
)
async def get_document(object_id: ObjectIdField):
    """

    :param object_id:
    :return:
    """
    try:
        return await retrieve_document(object_id, collection)
    except (ValueError, TypeError) as exception:
        raise NotFoundHTTPException(msg=str(exception)) from exception


# TODO: PUT for replace aka set PATCH for update ?
