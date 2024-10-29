from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:root@localhost:5433/crud"

async_engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    async_engine, 
    expire_on_commit=False, 
    class_=AsyncSession
)

Base = declarative_base()

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session