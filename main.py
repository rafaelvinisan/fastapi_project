import uvicorn
from fastapi import FastAPI
import contas_router
from settings.database import Base, engine
from models.conta import Conta

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
def get_name() -> str:
    return 'Rafael'

app.include_router(contas_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
