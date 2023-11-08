from sqlalchemy import Column, Integer, String, Table
from src.adapter.driven.infra.database.sqlalchemy.orm import (
    mapper_registry
)
from src.core.domain.entities.user import User


def start_mapper():
    user: Table = Table(
        "user",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("email", String(255), nullable=False, unique=True),
        Column("password", String(255), nullable=False),
    )

    mapper_registry.map_imperatively(User, user)
