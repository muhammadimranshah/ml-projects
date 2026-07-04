from fastapi import APIRouter
from sqlalchemy import text

from app.database.database import engine

router = APIRouter()

@router.get("/database-test")
def database_test():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "message": "Database Connected Successfully"
    }