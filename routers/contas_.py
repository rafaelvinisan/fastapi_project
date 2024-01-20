from typing import List
from fastapi import APIRouter, Depends
from settings.dependencies import get_db
from data_objects.conta import Conta_request, Conta_response
from sqlalchemy.orm import Session
from models.conta import Conta

router = APIRouter(prefix='/contas')

@router.get('/', response_model=List[Conta_response])
def list(db: Session = Depends(get_db)) -> List[Conta_response]:
    return db.query(Conta).all()

@router.post('/', response_model=Conta_response, status_code=201)
def add(conta: Conta_request, db: Session = Depends(get_db)) -> Conta_response:
    new_conta = Conta(**conta.dict())
    db.add(new_conta)
    db.commit()
    db.refresh(new_conta)
    return new_conta

@router.put('/{id}', response_model=Conta_response, status_code=200)
def update(id: int, conta: Conta_request, db: Session = Depends(get_db)) -> Conta_response:
    update_conta = db.query(Conta).get(id)
    update_conta.title = conta.title
    update_conta.value = conta.value
    update_conta.type = conta.type
    db.add(update_conta)
    db.commit()
    db.refresh(update_conta)
    return update_conta

@router.delete('/{id}', status_code=200)
def delete(id: int, db: Session = Depends(get_db)) -> None:
    conta = db.query(Conta).get(id)
    db.delete(conta)
    db.commit()

    