from fastapi.testclient import TestClient
from serving.main import app

client = TestClient(app)

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}  # Fixed case "OK"

def test_model_get():
    response = client.get("/model")
    assert response.status_code == 200
