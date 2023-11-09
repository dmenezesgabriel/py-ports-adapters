from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


engine = create_engine(
    "sqlite:///./app.db", echo=True, connect_args={"check_same_thread": False}
)
