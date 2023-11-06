from typing import List

from src.core.domain.entities.user import User
from src.core.application.ports.user_service import UserServiceInterface
from src.core.application.ports.user_repository import UserRepositoryInterface


class UserService(UserServiceInterface):
    """User use case or service implementation."""
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get_user(user_id)

    def get_users(self) -> List[User]:
        return self.user_repository.get_users()

    def create_user(self, user: User) -> User:
        return self.user_repository.create_user(user)

    def update_user(self, user: User) -> User:
        return self.user_repository.update_user(user)

    def delete_user(self, user_id: int) -> bool:
        return self.user_repository.delete_user(user_id)
