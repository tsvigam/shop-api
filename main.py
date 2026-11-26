from fastapi import FastAPI, HTTPException
import json

app= FastAPI()

@app.get("/products")
def get_products():
    with open("products.json", "r") as file:
        data = json.load(file)
    return data
@app.get("/products/{id}")
def get_product_by_id(id: int):
    with open("products.json", "r") as file:
        data = json.load(file)
    product=next((product for product in data if product["id"]==id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product was not found")
    else:
        return product
   