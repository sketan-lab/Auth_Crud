from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# ------------------------------
# FIX: Database URL must NOT contain schema.
# ------------------------------
DATABASE_URL = "postgresql://postgres:Ketan%40123@localhost:5432/Fastdb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Token config
SECRET_KEY = "Ketan"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 60
