import uvicorn
from fastapi import FastAPI
from routers import contas, fornecedor_cliente
#from models.conta import Conta

from settings.exceptions import DBEmpty, NotFound
from settings.exceptions_handler import not_found_exception_handler

app = FastAPI()

@app.get('/')
def get_name() -> str:
    return 'Rafael'

app.include_router(contas.router)
app.include_router(fornecedor_cliente.router)
app.add_exception_handler(NotFound, not_found_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
