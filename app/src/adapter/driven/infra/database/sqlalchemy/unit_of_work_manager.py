from sqlalchemy.orm import sessionmaker
from src.adapter.driven.infra.database.sqlalchemy.orm import engine
from src.core.application.ports.unit_of_work_manager import UnitOfWorkManager
from src.adapter.driven.infra.database.sqlalchemy.unit_of_work import (
    SQLAlchemyUnitOfWork
)


class SQLAlchemyUnitOfWorkManager(UnitOfWorkManager):
    _engine = engine

    def __init__(self) -> None:
        self._session_factory = sessionmaker(
            bind=self._engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False
        )

    def start(self):
        SessionLocal = self._session_factory()
        return SQLAlchemyUnitOfWork(session=SessionLocal)
