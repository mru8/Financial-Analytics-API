from pydantic import BaseModel
from datetime import date

class AssetBase(BaseModel):
    name: str
    sector: str
    price: float
    quantity: float
    date: date

class AssetCreate(AssetBase):
    pass

class AssetResponse(AssetBase):
    id: int

    class Config:
        orm_mode = True
