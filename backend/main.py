from fastapi import FastAPI

from routes.home import router as home_router
from routes.auth import router as auth_router

from database.connection import engine
from database.base import Base
import database.models

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Placement Preparation Agent",
    version="1.0.0"
)

# Register routers
app.include_router(home_router)
app.include_router(auth_router)