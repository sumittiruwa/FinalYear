from pydantic import BaseModel


# =====================================
# SHOP / PHARMACY
# =====================================

class ShopCreate(BaseModel):
    name: str
    owner: str | None = None
    category: str
    phone: str | None = None
    address: str
    latitude: float
    longitude: float


class ShopResponse(ShopCreate):
    id: int

    class Config:
        from_attributes = True


# =====================================
# MEDICINE
# =====================================

class MedicineCreate(BaseModel):
    shop_id: int
    name: str
    generic_name: str | None = None
    strength: str | None = None
    price: float
    stock: int


class MedicineResponse(BaseModel):
    id: int
    shop_id: int
    name: str
    generic_name: str | None = None
    strength: str | None = None
    price: float
    stock: int

    class Config:
        from_attributes = True