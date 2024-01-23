from pydantic import BaseModel, Field

class FornecedorCliente_response(BaseModel):
    ID: int
    name: str

    class Config:
        orm_mode = True


class FornecedorCliente_request(BaseModel):
    name: str 