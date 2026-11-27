from fastapi.testclient import TestClient
from main import app


def test_get_products():
    client = TestClient(app)
    response = client.get("/products")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Eraser", "price": 5},
        {"id": 2, "name": "Pencil", "price": 3},
	{"id": 3, "name": "Ruler", "price": 1},
	{"id": 4, "name": "Pen", "price": 7}]
def test_get_product():
    client=TestClient(app)
    response = client.get("/products/2")
    assert response.status_code == 200
    assert response.json() == {"id": 2, "name": "Pencil", "price": 3}
def test_get_missing_product():
    client = TestClient(app)
    response = client.get("products/5")
    assert response.status_code == 404
    assert response.json() == {"detail":"Product was not found"}