import app.routes.assets as assets
print(f"DEBUG: Loading assets file from: {assets.__file__}")
from fastapi import FastAPI
from app.database import engine
from app import models
import app.routes.assets as assets_module

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Financial Portfolio Analytics API")

# Use the new name we just created
app.include_router(assets_module.assets_router_obj)

@app.get("/")
def root():
    return {"status": "success"}