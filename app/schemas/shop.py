from pydantic import BaseModel


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