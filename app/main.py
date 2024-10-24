from fastapi import FastAPI
from routers import product

app = FastAPI()
app.include_router(product)

@app.get("/healthy")
async def health_check():
    return {"status": "Healthy"}