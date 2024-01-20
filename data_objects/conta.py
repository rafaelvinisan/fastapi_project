from enum import Enum
from pydantic import BaseModel, Field

class Tipo_enum(str, Enum):
    pagar = "pagar"
    receber = "receber"

class Conta_response(BaseModel):
    ID: int
    title: str
    value: float
    type: str

    class Config:
        orm_mode = True


class Conta_request(BaseModel):
    title: str 
    value: float = Field(gt=0)
    type: Tipo_enum