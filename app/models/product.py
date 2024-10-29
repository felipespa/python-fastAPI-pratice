from sqlalchemy import Column, Integer, Numeric, String
from ..database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    description = Column(String, nullable=True)

    def __repr__(self):
        return f"<Product(nome={self.name}, price={self.price}, description={self.description})>"
