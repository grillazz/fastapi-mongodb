from bson import ObjectId
from bson.errors import InvalidId
from pydantic import BaseModel, Field


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

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class DocumentResponse(Document):
    id: ObjectIdField = Field(...)
