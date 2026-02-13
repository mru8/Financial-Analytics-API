from sqlalchemy import text  
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db  # Import from your database.py
from app import models
import app.routes.assets as assets_module

# 1. THE BUILDER: This creates your tables in the empty Koyeb database
# It uses the 'Base' and 'engine' you defined in database.py
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Financial Portfolio Analytics API")

# 2. THE ROUTES: Connect your existing asset logic
app.include_router(assets_module.assets_router_obj)

@app.get("/")
def root():
    return {"status": "success", "info": "Financial API is Live"}

# 3. THE BRIDGE TEST: Add this to verify the connection on Koyeb
@app.get("/test-db")
def test_connection(db: Session = Depends(get_db)):
    try:
        # Wrap the query in the text() function
        result = db.execute(text("SELECT 1")).fetchone() 
        return {"status": "connected", "database_response": result[0]}
    except Exception as e:
        return {"status": "error", "detail": str(e)}