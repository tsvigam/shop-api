from fastapi import FastAPI

app= FastAPI()

@app.get("/products")
def get_products():
    return [{"id": 1, "name": "Eraser", "price": 5},{"id": 2, "name": "Pencil", "price": 3}]