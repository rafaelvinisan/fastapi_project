from fastapi.testclient import TestClient
from sqlalchemy import create_engine, orm
from settings.database import Base
from settings.dependencies import get_db
from settings.envs import env

from main import app

client = TestClient(app)

engine = create_engine(env.TEST_DB_URL)

TestingSessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

def test_list_contas():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    novas_contas = [
        {"title":"Cruzeiro do Neymar", "value":500, "type":"pagar"},
        {"title":"Programa", "value":500, "type":"receber"}
    ]
    
    [client.post('/contas', json=nova_conta) for nova_conta in novas_contas]

    response = client.get('/contas')
    assert response.status_code == 200
    assert response.json() == [
        {"ID":1, "title":"Cruzeiro do Neymar", "value":500, "type":"pagar"},
        {"ID":2, "title":"Programa", "value":500, "type":"receber"}
    ]

def test_error_invalid_type():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    json = {"title":"Cruzeiro do Neymar", "value":500, "type":"Pagando"}
    response = client.post('/contas', json=json)

    assert response.status_code == 422

def test_update_conta():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    json = {"title":"Cruzeiro do Neymar", "value":500, "type":"pagar"}
    response = client.post('/contas', json=json)
    id = response.json()['ID']

    assert response.json()['title'] == "Cruzeiro do Neymar"

    json_new_title = {"title":"Passeio de Navio do Neymar", "value":500, "type":"pagar"}
    response_put = client.put(f'/contas/{id}', json = json_new_title)
    
    assert response_put.status_code == 200
    assert response_put.json()['title'] == "Passeio de Navio do Neymar"

def test_delete_conta():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    novas_contas = [
        {"title":"Cruzeiro do Neymar", "value":500, "type":"pagar"},
        {"title":"Programa", "value":500, "type":"receber"}
    ]
    
    [client.post('/contas', json=nova_conta) for nova_conta in novas_contas]

    response_get = client.get('/contas')
    assert len(response_get.json()) == len(novas_contas)

    response_delete = client.delete(f'/contas/1')
    assert response_delete.status_code == 200
    
    response_get = client.get('/contas')
    assert len(response_get.json()) == len(novas_contas) - 1

    

