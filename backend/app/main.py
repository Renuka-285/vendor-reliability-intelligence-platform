from fastapi import FastAPI

from app.database import Base
from app.database import engine

from models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Vendor Reliability Platform API"
    }