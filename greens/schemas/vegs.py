from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field, root_validator

from bson import ObjectId
from bson.errors import InvalidId


class ObjectIdField(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        try:
            return ObjectId(str(value))
        except InvalidId:
            raise ValueError("Not a valid ObjectId")


class Document(BaseModel):
    name: str = Field(...)
    desc: str = Field(...)

    # @root_validator()
    # def validation(cls, values):
    #     if values["id"] and not ObjectId.is_valid(values["id"]):
    #         raise ValueError("Research Object ID is not valid.")
    #     return values

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class DocumentResponse(Document):
    id: ObjectIdField = Field(...)
