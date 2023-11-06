from typing import List
from src.core.application.ports.user_repository import UserRepositoryInterface
from src.core.domain.entities.user import User


class UserRepository(UserRepositoryInterface):
    """User repository implementation."""

    def get_by_id(self, id: int) -> User:
        return User(email="example1@example.com", password="123")

    def get_all(self) -> List[User]:
        return [
            User(email="example1@example.com", password="123"),
            User(email="example1@example.com", password="123"),
        ]

    def create(self, user: User) -> User:
        raise NotImplementedError

    def update(self, user: User) -> User:
        raise NotImplementedError

    def delete(self, id: int) -> bool:
        raise NotImplementedError
