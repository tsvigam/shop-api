from fastapi import FastAPI
import json

app= FastAPI()

@app.get("/products")
def get_products():

    with open("products.json", "r") as file:
        data = json.load(file)

    return data