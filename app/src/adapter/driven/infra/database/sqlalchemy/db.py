from sqlalchemy.orm import registry
from sqlalchemy import create_engine

mapper_registry = registry()

engine = create_engine(
        'sqlite:///./app.db',
        echo=True,
        connect_args={"check_same_thread": False}
    )


def create_db_and_tables():
    mapper_registry.metadata.create_all(engine)
