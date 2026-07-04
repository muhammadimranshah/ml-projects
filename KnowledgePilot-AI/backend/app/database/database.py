from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

from urllib.parse import quote_plus
from app.database.base import Base
from app.models import User
from sqlalchemy.orm import Session

password = quote_plus(settings.DATABASE_PASSWORD)

DATABASE_URL = (
    f"postgresql://{settings.DATABASE_USER}:"
    f"{password}@"
    f"{settings.DATABASE_HOST}:"
    f"{settings.DATABASE_PORT}/"
    f"{settings.DATABASE_NAME}"
)
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)



Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()