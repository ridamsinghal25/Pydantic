from pydantic import BaseModel # type: ignore

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

input_data = {
    "id": 102,
    "name": "Laptop",
    "price": 30000
}

product = Product(**input_data)
print(product)