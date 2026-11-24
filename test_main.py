from fastapi.testclient import TestClient
from main import app


def test_get_products():
    client = TestClient(app)
    response = client.get("/products")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Eraser", "price": 5},
        {"id": 2, "name": "Pencil", "price": 3},
    ]