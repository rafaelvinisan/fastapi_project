from pydantic import BaseModel

class Conta_response(BaseModel):
    ID: int
    title: str
    value: float
    type: str

    class Config:
        orm_mode = True


class Conta_request(BaseModel):
    title: str
    value: float
    type: str