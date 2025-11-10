# main.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Generic, TypeVar
from datetime import datetime, timedelta
import random

app = FastAPI(title="Demo API for Playwright Mocking")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "https://api-mocking-demo-app.netlify.app"],  # Angular dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos
class User(BaseModel):
    id: int
    name: str
    email: str
    role: str
    status: str
    createdAt: str

class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float
    stock: int
    supplier: str

T = TypeVar('T')

class GridResponse(BaseModel, Generic[T]):
    data: List[T]
    total: int
    page: int
    pageSize: int

# Datos de ejemplo
USERS_DATA = [
    {
        "id": i,
        "name": f"{random.choice(['John', 'Jane', 'Mike', 'Sarah', 'David', 'Emma'])} {random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia'])}",
        "email": f"user{i}@example.com",
        "role": random.choice(['Admin', 'User', 'Manager', 'Developer']),
        "status": random.choice(['Active', 'Inactive', 'Pending']),
        "createdAt": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d")
    }
    for i in range(1, 101)
]

PRODUCTS_DATA = [
    {
        "id": i,
        "name": f"{random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam', 'Tablet', 'Phone'])} {random.choice(['Pro', 'Ultra', 'Max', 'Plus', 'Premium', 'Basic'])}",
        "category": random.choice(['Electronics', 'Accessories', 'Office', 'Gaming']),
        "price": round(random.uniform(10, 2000), 2),
        "stock": random.randint(0, 200),
        "supplier": f"{random.choice(['TechCorp', 'GlobalSupply', 'MegaDistributor', 'PrimeVendor', 'EliteSource'])} Inc."
    }
    for i in range(1, 101)
]

# Endpoints
@app.get("/")
def read_root():
    return {
        "message": "Demo API for Playwright Mocking",
        "endpoints": {
            "users": "/api/users",
            "products": "/api/products"
        }
    }

@app.get("/api/users", response_model=GridResponse[User])
def get_users(
    page: int = Query(1, ge=1),
    pageSize: int = Query(10, ge=1, le=100)
):
    """
    Obtiene la lista de usuarios con paginación
    """
    start_idx = (page - 1) * pageSize
    end_idx = start_idx + pageSize
    
    paginated_data = USERS_DATA[start_idx:end_idx]
    
    return GridResponse(
        data=paginated_data,
        total=len(USERS_DATA),
        page=page,
        pageSize=pageSize
    )

@app.get("/api/products", response_model=GridResponse[Product])
def get_products(
    page: int = Query(1, ge=1),
    pageSize: int = Query(10, ge=1, le=100)
):
    """
    Obtiene la lista de productos con paginación
    """
    start_idx = (page - 1) * pageSize
    end_idx = start_idx + pageSize
    
    paginated_data = PRODUCTS_DATA[start_idx:end_idx]
    
    return GridResponse(
        data=paginated_data,
        total=len(PRODUCTS_DATA),
        page=page,
        pageSize=pageSize
    )

# Endpoints adicionales para casos de prueba
@app.get("/api/users/slow")
def get_users_slow():
    """
    Endpoint que simula lentitud (útil para testing)
    """
    import time
    time.sleep(3)
    return GridResponse(
        data=USERS_DATA[:10],
        total=len(USERS_DATA),
        page=1,
        pageSize=10
    )

@app.get("/api/products/error")
def get_products_error():
    """
    Endpoint que simula un error (útil para testing)
    """
    from fastapi import HTTPException
    raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)