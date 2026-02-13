from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

assets_router_obj = APIRouter(prefix="/assets", tags=["Assets"])

@assets_router_obj.post("/", response_model=schemas.AssetResponse)
def create_asset(asset: schemas.AssetCreate, db: Session = Depends(get_db)):
    db_asset = models.Asset(**asset.dict())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@assets_router_obj.get("/", response_model=list[schemas.AssetResponse])
def get_assets(db: Session = Depends(get_db)):
    return db.query(models.Asset).all()
