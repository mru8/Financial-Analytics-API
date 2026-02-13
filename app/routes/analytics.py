from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..services import analytics_service

router = APIRouter(prefix="/portfolio", tags=["Analytics"])

@router.get("/value")
def portfolio_value(db: Session = Depends(get_db)):
    assets = db.query(models.Asset).all()
    return {"total_value": analytics_service.calculate_portfolio_value(assets)}

@router.get("/sector-breakdown")
def sector(db: Session = Depends(get_db)):
    assets = db.query(models.Asset).all()
    return analytics_service.sector_breakdown(assets)

@router.get("/top-assets")
def top_assets(db: Session = Depends(get_db)):
    assets = db.query(models.Asset).all()
    return analytics_service.top_assets(assets)

@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    assets = db.query(models.Asset).all()
    return analytics_service.portfolio_summary(assets)
