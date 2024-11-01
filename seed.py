import asyncio
from app.models.product import Product
from app.database import get_session

async def seed_db():

    async for db in get_session():
    
        try:
            products = [
                Product(name="Product 1", price=19.99, description="Description for Product 1"),
                Product(name="Product 2", price=29.99, description="Description for Product 2"),
                Product(name="Product 3", price=39.99, description="Description for Product 3"),
                Product(name="Product 4", price=49.99, description="Description for Product 4"),
                Product(name="Product 5", price=59.99, description="Description for Product 5")
            ]

            db.add_all(products)
            await db.commit()
        except Exception as e:
            await db.rollback()
            print(f"Error seeding database: {e}")
        finally:
            await db.close()

if __name__ == "__main__":
    asyncio.run(seed_db())