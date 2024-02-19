from bson import ObjectId as _ObjectId
from pydantic import BaseModel, ConfigDict, BeforeValidator
from typing_extensions import Annotated


# def check_object_id(value: str) -> str:
#     if not _ObjectId.is_valid(value):
#         raise ValueError('Invalid ObjectId')
#     return value


def check_object_id(value: _ObjectId) -> str:
    """
    Checks if the given _ObjectId is valid and returns it as a string.

    Args:
        value: The _ObjectId to be checked.

    Returns:
        str: The _ObjectId as a string.

    Raises:
        ValueError: If the _ObjectId is invalid.
    """

    if not _ObjectId.is_valid(value):
        raise ValueError("Invalid ObjectId")
    return str(value)


ObjectIdField = Annotated[str, BeforeValidator(check_object_id)]

config = ConfigDict(arbitrary_types_allowed=True, populate_by_name=True)


class Document(BaseModel):
    model_config = config

    name: str
    desc: str


class DocumentResponse(BaseModel):
    id: ObjectIdField
