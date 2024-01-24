from pydantic import BaseModel
from typing import Any, Dict, List

class Conta_response(BaseModel):
    ID: int
    title: str
    value: float
    type: str

class Conta_request(BaseModel):
    title: str
    value: float
    type: str

def add_conta(contas_list: List[Conta_response], attributes: Dict[str, Any]) -> None:
    global id
    id += 1
    attributes['ID'] = id
    contas_list.append(Conta_response(**attributes))

id = 0