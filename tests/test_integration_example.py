import pytest
from app import app, items

@pytest.fixture
def client():
    """Configure Flask test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        items.clear() 
        yield client

def test_index_endpoint(client):
    """Test de l'endpoint GET /"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Items" in response.data

def test_add_endpoint(client):
    """Test de l'endpoint POST /add"""
    response = client.post("/add", data={"item": "TestItem"}, follow_redirects=True)
    assert response.status_code == 200
    assert "TestItem" in items
