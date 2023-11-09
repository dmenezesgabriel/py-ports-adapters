from sqlalchemy import Column, Integer, String
from src.adapter.driven.infra.database.sqlalchemy.orm import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
