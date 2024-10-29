from fastapi import FastAPI
from .routers import product

app = FastAPI()
app.include_router(product.router)

@app.get("/healthy")
async def health_check():
    return {"status": "Healthy"}