from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..business.product import ProductItem, create_product, delete_product, get_product, get_product_by_id, update_product

router = APIRouter(prefix="/product", tags=["product"])

@router.get("/", response_model=dict, status_code=status.HTTP_200_OK)
async def list_product(db: AsyncSession = Depends(get_db)):
    result = await get_product(db)

    if not result["success"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result['message'])
    return result

@router.get("/{product_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def list_product_by_id(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await get_product_by_id(product_id, db)
    if not result['success']:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result['message'])
    return result

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def add_product(product: ProductItem, db: AsyncSession = Depends(get_db)):
    result = await create_product(product, db)
    if not result['success']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result['message'])
    return result

@router.put("/{product_id}", response_model=dict, status_code=status.HTTP_200_OK)
async def update_product(product_id: int, product: ProductItem, db: AsyncSession = Depends(get_db)):
    result = await update_product(product_id, product, db)
    if not result['success']:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result['message'])
    return result

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_product(product_id: int, db: AsyncSession = Depends(get_db)):
    result = await delete_product(product_id, db)
    if not result['success']:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result['message'])