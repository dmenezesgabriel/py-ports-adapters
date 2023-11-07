from typing import List
from src.core.application.ports.user_repository import UserRepositoryInterface
from src.core.domain.entities.user import User


class UserRepository(UserRepositoryInterface):
    """User repository implementation."""
    def __init__(self, work_manager):
        self._work_manager = work_manager

    def get_by_id(self, id: int) -> User:
        with self._work_manager.start() as session:
            return session.query(User).filter_by(id=id).first()

    def get_all(self) -> List[User]:
        return [
            User(email="example1@example.com", password="123"),
            User(email="example1@example.com", password="123"),
        ]

    def create(self, user: User) -> User:
        with self._work_manager.start() as session:
            session.add(user)
        return user

    def update(self, user: User) -> User:
        with self._work_manager.start() as session:
            session.add(user)
            return user

    def delete(self, id: int) -> bool:
        with self._work_manager.start() as session:
            user = session.query(User).filter_by(id=id).first()
            session.delete(user)
            return True
