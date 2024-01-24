from typing import List
from fastapi import APIRouter
from models import Conta_request, Conta_response, add_conta

router = APIRouter(prefix='/contas')


contas = list()
add_conta(contas,{"title":"Aluguel", "value":1200, "type":"pagar"})
add_conta(contas,{"title":"Mercado", "value":500, "type":"receber"})

@router.get('/', response_model=List[Conta_response])
def list():
    return contas

@router.post('/', response_model=Conta_response)
def add(conta: Conta_request):
    add_conta(contas, conta.dict())
    return contas[-1]