from src.adapter.driven.infra.database.sqlalchemy.orm import (
    mapper_registry, engine
)
from src.adapter.driven.infra.database.sqlalchemy.models.user import (
    start_mapper
)
from src.adapter.driven.infra.database.sqlalchemy.unit_of_work_manager import (
    SQLAlchemyUnitOfWorkManager
)
from src.core.domain.entities.user import User
from src.adapter.driven.infra.database.sqlalchemy.repositories.user import (
    UserRepository
)


def test_orm():
    start_mapper()
    mapper_registry.metadata.create_all(engine)

    unit_of_work = SQLAlchemyUnitOfWorkManager()
    user_repository = UserRepository(unit_of_work)

    user = User(
        email="test@example.com",
        password="123456",
    )
    user_repository.create(user)
