from fastapi import FastAPI
import json

app = FastAPI()

# Cargar productos desde archivo JSON
def load_products():
    with open("products.json", "r") as f:
        return json.load(f)

@app.get("/products")
def get_products(order_by: str = "name"):
    products = load_products()
    if order_by == "price":
        products.sort(key=lambda x: x["price"])
    else:
        products.sort(key=lambda x: x["name"].lower())
    return products

# Para ejecutar: `uvicorn server:app --reload`
