import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL, echo=True
)
