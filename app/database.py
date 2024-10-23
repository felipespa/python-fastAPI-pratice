from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://root:root@localhost:5432/crud"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

Base = declarative_base()

def get_db():
    db = async_session()
    try:
        yield db
    finally:
        db.close()