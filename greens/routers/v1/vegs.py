
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_201_CREATED

from greens import config
from greens.routers.exceptions import NotFoundHTTPException
from greens.schemas.vegs import DocumentResponse, ObjectIdField, Document
from greens.services.repository import retrieve_document, create_document


global_settings = config.get_settings()
collection = global_settings.collection

router = APIRouter()


@router.post("/",
             status_code=HTTP_201_CREATED,
             response_description="Document created",
             response_model=DocumentResponse,
)
async def add_document(payload: Document):
    try:
        payload = jsonable_encoder(payload)
        return await create_document(payload, collection)
    except ValueError as exception:
        raise NotFoundHTTPException(msg=str(exception))


@router.get(
    "/{object_id}",
    response_description="Document retrieved",
    response_model=DocumentResponse,
)
async def get_document(object_id: ObjectIdField):
    try:
        return await retrieve_document(object_id, collection)
    except ValueError as exception:
        raise NotFoundHTTPException(msg=str(exception))



    # try:
    #     assert 5 / 0
    # except Exception:
    #     logger.exception("My way or highway...")