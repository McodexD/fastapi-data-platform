from fastapi import FastAPI
from pydantic import BaseModel
from psycopg_pool import ConnectionPool
import json


DATABASE_URL = "postgresql://elev@localhost:5432/demo_5"


pool = ConnectionPool(DATABASE_URL)

app = FastAPI()



class DimensionsSchema(BaseModel):
    width_cm: float
    height_cm: float
    depth_cm: float

class ProductSchema(BaseModel):
    product_id: str
    name: str
    price: float
    currency: str
    tags: list[str] | None = None
    # Add this line to include the dimensions box inside the product box
    dimensions: DimensionsSchema | None = None


@app.post("/products")
def create_product(product: ProductSchema):
    
    product_data = product.model_dump()
    
    with pool.connection() as conn:
        conn.execute(
            "INSERT INTO products_raw (product) VALUES (%s)",
            (json.dumps(product_data),)
        )
    return {"status": "success", "data_saved": product_data}


@app.get("/products")
def get_products():
    with pool.connection() as conn:
        results = conn.execute("SELECT * FROM products_raw;").fetchall()
        return results