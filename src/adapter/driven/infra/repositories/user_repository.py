from typing import List
from core.application.ports.user_repository import UserRepositoryInterface
from core.domain.entities.user import User


class UserRepository(UserRepositoryInterface):
    """User repository implementation."""
    def get_user(self, user_id: int) -> User:
        raise NotImplementedError

    def get_users(self) -> List[User]:
        raise NotImplementedError

    def create_user(self, user: User) -> User:
        raise NotImplementedError

    def update_user(self, user: User) -> User:
        raise NotImplementedError

    def delete_user(self, user_id: int) -> bool:
        raise NotImplementedError
