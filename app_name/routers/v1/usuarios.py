from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_201_CREATED

from app_name.routers.exceptions import NotFoundHTTPException
from app_name.schemas.usuarios import Usuario
from app_name.services.repository import create_document


router = APIRouter()
collection = "usuarios"


@router.post(
    "",
    status_code=HTTP_201_CREATED,
    response_description="Document created",
    response_model=Usuario,
)
async def add_document(payload: Usuario):
    """

    :param payload:
    :return:
    """
    try:
        payload = jsonable_encoder(payload)
        return await create_document(payload, collection)
    except ValueError as exception:
        raise NotFoundHTTPException(msg=str(exception))
