from typing import List
from fastapi import APIRouter, Depends
from settings.dependencies import get_db
from data_objects.fornecedor_cliente import FornecedorCliente_request, FornecedorCliente_response
from sqlalchemy.orm import Session
from models.fornecedor_cliente import FornecedorCliente
from settings.exceptions import NotFound

router = APIRouter(prefix='/fornecedor_cliente')

def find_fornecedor_cliente_from_id(id: int, db) -> FornecedorCliente_response:
    fornecedor_cliente = db.query(FornecedorCliente).get(id)
    if fornecedor_cliente is None:
        raise NotFound(f"ID: {id}")
    else:
        return fornecedor_cliente

@router.get('/', response_model=List[FornecedorCliente_response])
def list(db: Session = Depends(get_db)) -> List[FornecedorCliente_response]:
    all_fornecedor_cliente = db.query(FornecedorCliente).all()
    return all_fornecedor_cliente

@router.get('/{id}', response_model=FornecedorCliente_response)
def get(id:int, db: Session = Depends(get_db)) -> FornecedorCliente_response:
    return find_fornecedor_cliente_from_id(id, db)


@router.post('/', response_model=FornecedorCliente_response, status_code=201)
def add(fornecedor_cliente: FornecedorCliente_request, db: Session = Depends(get_db)) -> FornecedorCliente_response:
    new_fornecedor_cliente = FornecedorCliente(**fornecedor_cliente.dict())
    db.add(new_fornecedor_cliente)
    db.commit()
    db.refresh(new_fornecedor_cliente)
    return new_fornecedor_cliente

@router.put('/{id}', response_model=FornecedorCliente_response, status_code=200)
def update(id: int, fornecedor_cliente: FornecedorCliente_request, db: Session = Depends(get_db)) -> FornecedorCliente_response:
    update_fornecedor_cliente = find_fornecedor_cliente_from_id(id,db)
    update_fornecedor_cliente.name = fornecedor_cliente.name
    db.add(update_fornecedor_cliente)
    db.commit()
    db.refresh(update_fornecedor_cliente)
    return update_fornecedor_cliente

@router.delete('/{id}', status_code=200)
def delete(id: int, db: Session = Depends(get_db)) -> None:
    fornecedor_cliente = find_fornecedor_cliente_from_id(id, db)
    db.delete(fornecedor_cliente)
    db.commit()

    