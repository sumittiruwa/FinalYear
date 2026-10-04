from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base


# =====================================
# SHOP / PHARMACY
# =====================================

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


# =====================================
# MEDICINE INVENTORY
# =====================================

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)

    shop_id = Column(
        Integer,
        ForeignKey("shops.id"),
        nullable=False
    )

    name = Column(String, nullable=False)

    generic_name = Column(
        String,
        nullable=True
    )

    strength = Column(
        String,
        nullable=True
    )

    price = Column(
        Float,
        nullable=False
    )

    stock = Column(
        Integer,
        nullable=False,
        default=0
    )