from typing import List
from fastapi import APIRouter, Depends
from config.dependencies import get_db
from data_objects.conta import Conta_request, Conta_response, add_conta
from sqlalchemy.orm import Session
from models.conta import Conta

router = APIRouter(prefix='/contas')


contas = list()
add_conta(contas,{"title":"Aluguel", "value":1200, "type":"pagar"})
add_conta(contas,{"title":"Mercado", "value":500, "type":"receber"})

@router.get('/', response_model=List[Conta_response])
def list():
    return contas

@router.post('/', response_model=Conta_response, status_code=201)
def add(conta: Conta_request, db: Session = Depends(get_db)) -> Conta_response:
    new_conta = Conta(**conta.dict())
    db.add(new_conta)
    db.commit()
    db.refresh(new_conta)
    return Conta_response(**new_conta.__dict__)