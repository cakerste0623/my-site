import os
from server import app

client = app.test_client()

def test_login():
    response = client.post('/login', json={"username": os.environ['DB_USERNAME'], "password": os.environ['DB_PWD']})
    assert response.status_code == 200
    assert response.json['token'] is not None

    response = client.post('/login', json={"username": "1", "password": "1"})
    assert response.status_code == 401
