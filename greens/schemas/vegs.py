from bson import ObjectId as _ObjectId
from bson.errors import InvalidId
from pydantic import BaseModel, Field, ConfigDict, AfterValidator
from typing_extensions import Annotated


# class ObjectIdField(str):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate
#
#     @classmethod
#     def validate(cls, value):
#         try:
#             return ObjectId(str(value))
#         except InvalidId as e:
#             raise ValueError("Not a valid ObjectId") from e


def check_object_id(value: str) -> str:
    if not _ObjectId.is_valid(value):
        raise ValueError('Invalid ObjectId')
    return value


ObjectIdField = Annotated[str, AfterValidator(check_object_id)]


config = ConfigDict(arbitrary_types_allowed=True, populate_by_name=True)


class Document(BaseModel):
    # model_config = config

    name: str = Field(...)
    desc: str = Field(...)


class DocumentResponse(Document):
    id: ObjectIdField
