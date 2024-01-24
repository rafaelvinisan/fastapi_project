import uvicorn
from fastapi import FastAPI
import contas

app = FastAPI()

@app.get('/')
def get_name() -> str:
    return 'Rafael'

app.include_router(contas.router)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
