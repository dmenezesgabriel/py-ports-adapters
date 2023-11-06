from typing import List
from src.core.application.ports.user_repository import UserRepositoryInterface
from src.core.domain.entities.user import User


class UserRepository(UserRepositoryInterface):
    """User repository implementation."""

    def get_user(self, user_id: int) -> User:
        return User(email="example1@example.com", password="123")

    def get_users(self) -> List[User]:
        return [
            User(email="example1@example.com", password="123"),
            User(email="example1@example.com", password="123"),
        ]

    def create_user(self, user: User) -> User:
        raise NotImplementedError

    def update_user(self, user: User) -> User:
        raise NotImplementedError

    def delete_user(self, user_id: int) -> bool:
        raise NotImplementedError
