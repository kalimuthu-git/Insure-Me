import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_policy(client):
    response = client.post('/createPolicy', json={
        "name": "Test Policy",
        "type": "Life",
        "amount": 10000
    })
    assert response.status_code == 201