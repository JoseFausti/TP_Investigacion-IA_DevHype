# Backend (Python - FastAPI):
# main.py
from fastapi import FastAPI, HTTPException # type: ignore
from typing import List, Dict
import json

app = FastAPI(title="Product Sorter API")

# Cargar productos desde JSON
def load_products():
    try:
        with open("products.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.get("/products")
async def get_products(sort_by: str = "name", ascending: bool = True):
    products = load_products()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    
    if sort_by == "name":
        products.sort(key=lambda x: x["name"], reverse=not ascending)
    elif sort_by == "price":
        products.sort(key=lambda x: x["price"], reverse=not ascending)
    else:
        raise HTTPException(status_code=400, detail="Invalid sort_by parameter")
    
    return products
