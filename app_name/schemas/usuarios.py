import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Usuario(BaseModel):
    # id: str = Field(default_factory=uuid.uuid4, alias="_id")
    nome: str = Field(max_length=100)
    telefone: str = Field(max_length=14)
    congregacao: str = Field(...)
    coordenador: bool = Field(default=False)
    numero_carne: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "nome": "Don Quixote",
                "telefone": "79998480537",
                "congregacao": "Sede",
                "coordenador": False,
                "numero_carne": "000001",
            }
        }


class UsuarioUpdate(BaseModel):
    nome: Optional[str]
    telefone: Optional[str]
    congregacao: Optional[str]
    coordenador: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "nome": "Don Quixote",
                "telefone": "79998480537",
                "congregacao": "Sede",
                "coordenador": False,
            }
        }
