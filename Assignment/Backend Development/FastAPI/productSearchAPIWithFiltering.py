from fastapi import FastAPI
from typing import Optional

app=FastAPI()

products_db = [
    {"id": 1, "name": "Laptop Pro", "category": "electronics", "price": 75000},
    {"id": 2, "name": "Wireless Mouse", "category": "electronics", "price": 1200},
    {"id": 3, "name": "Bluetooth Headphones", "category": "electronics", "price": 3500},
    {"id": 4, "name": "Smartphone X", "category": "electronics", "price": 45000},
    {"id": 5, "name": "Tablet Mini", "category": "electronics", "price": 22000},

    {"id": 6, "name": "Office Chair", "category": "furniture", "price": 5500},
    {"id": 7, "name": "Study Table", "category": "furniture", "price": 8500},
    {"id": 8, "name": "Wooden Bed", "category": "furniture", "price": 28000},
    {"id": 9, "name": "Bookshelf", "category": "furniture", "price": 6000},
    {"id": 10, "name": "Sofa Set", "category": "furniture", "price": 45000},

    {"id": 11, "name": "Python Programming Book", "category": "books", "price": 650},
    {"id": 12, "name": "Data Science Handbook", "category": "books", "price": 900},
    {"id": 13, "name": "Machine Learning Guide", "category": "books", "price": 1200},
    {"id": 14, "name": "FastAPI in Action", "category": "books", "price": 800},
    {"id": 15, "name": "Database Systems", "category": "books", "price": 950},

    {"id": 16, "name": "Running Shoes", "category": "fashion", "price": 3000},
    {"id": 17, "name": "Sports T-Shirt", "category": "fashion", "price": 1200},
    {"id": 18, "name": "Denim Jeans", "category": "fashion", "price": 2500},
    {"id": 19, "name": "Leather Jacket", "category": "fashion", "price": 8500},
    {"id": 20, "name": "Sneakers", "category": "fashion", "price": 4000},
]

   
@app.get("/products/search")
def search(
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    keyword1: Optional[str] = None,
    limit: int = 10,
    skip: int = 0
    ):
    temp = products_db.copy()   

    if category is not None:
        temp = [i for i in temp if i["category"] == category]

    if keyword1 is not None:
        temp = [
            i for i in temp
            if keyword1.lower() in i["name"].lower()
        ]

    if min_price is not None:
        temp = [i for i in temp if i["price"] >= min_price]

    if max_price is not None:
        temp = [i for i in temp if i["price"] <= max_price]

    temp = temp[skip : skip + limit]

    return temp