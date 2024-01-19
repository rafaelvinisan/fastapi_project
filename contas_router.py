from typing import List
from fastapi import APIRouter, Depends
from config.dependencies import get_db
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