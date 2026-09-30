from sqlalchemy import Column, Integer, String, Float
from .database import Base


class Shop(Base):
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    owner = Column(String, nullable=True)
    category = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=False)

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)