import asyncio
from typing import List
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..models.product import Product, ProductSchema

class ProductItem(BaseModel):
    name: str
    price: float
    description: str


async def get_product(session: AsyncSession, limit: int = 10):
    query = select(Product).limit(limit)
    result = await session.execute(query)

    data = result.scalars().all()

    if not data:
        return {
            "success": False,
            "message": "No products found",
            "data": []
        }

    return {
        "success": True,
        "message": f"{len(data)} product(s) found",
        "data": data,
        "total": f"{len(data)}",
    }

async def get_product_by_id(product_id: int, session: AsyncSession):
    query = select(Product).filter(Product.id == product_id)
    result = await session.execute(query)

    product = result.scalars().first()

    if product is None:
        return {
            "success": False,
            "message": "Product not found",
            "data": None
        }

    return {
        "success": True,
        "message": "Product found",
        "data": product
    }

async def create_product(product: ProductItem, session: AsyncSession, ignore_commit=False):
    new_product = Product(
        name=product.name,
        price=product.price,
        description=product.description
    )
    
    session.add(new_product)

    if not ignore_commit:
        await session.commit()

    return {
        "success": True,
        "data": new_product,
        "message": "Product created successfully!"
    }

async def update_product(product_id: int, product: ProductItem, session: AsyncSession):
    result = await get_product_by_id(product_id, session)

    if not result["success"]:
        return {
            "success": False,
            "message": "Cannot update. Product not found",
            "data": None
        }

    existing_product = result["data"]
    existing_product.name = product.name
    existing_product.price = product.price
    existing_product.description = product.description

    await session.commit()
    return {
        "success": True,
        "message": "Product updated successfully!",
        "data": existing_product
    }

async def delete_product(product_id: int, session: AsyncSession):
    result = await get_product_by_id(product_id, session)

    if not result["success"]:
        return {
            "success": False,
            "message": "Cannot delete. Product not found"
        }


    product_to_delete = result["data"]

    await session.delete(product_to_delete)
    await session.commit()

    return {
        "success": True,
        "message": "Product deleted successfully!"
    }

async def bulk_create_products(productList: List[ProductItem], session: AsyncSession):
    async with session.begin():
        tasks = [create_product(product, session, ignore_commit=True) for product in productList]
        result_list = await asyncio.gather(*tasks)

    added_products = [
        ProductSchema.model_validate(result["data"].__dict__)
        for result in result_list if result["success"]
    ]

    product_names = ', '.join([product.name for product in added_products])

    return {
        "success": True,
        "message": f"Products added successfully: {product_names}",
        "data": added_products
    }

async def bulk_get_products_by_id(product_ids: List[int], session: AsyncSession):
    tasks = [get_product_by_id(product_id, session) for product_id in product_ids]
    result_list = await asyncio.gather(*tasks)

    product_list = [
        ProductSchema.model_validate(result["data"].__dict__)
        for result in result_list if result["success"]
    ]    

    if not product_list:
        return {
            "success": False,
            "message": "Error: No valid products found for the given IDs",
        }

    return {
        "success": True,
        "message": "Products found",
        "data": product_list
    }