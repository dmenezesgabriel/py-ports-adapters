import abc
from typing import List
from src.core.domain.entities.user import User


class UserServiceInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, __subclass: type) -> bool:
        return (
            hasattr(__subclass, 'get_user') and
            callable(__subclass.get_user) and
            hasattr(__subclass, 'get_users') and
            callable(__subclass.get_users) and
            hasattr(__subclass, 'create_user') and
            callable(__subclass.create_user) and
            hasattr(__subclass, 'update_user') and
            callable(__subclass.update_user) and
            hasattr(__subclass, 'delete_user') and
            callable(__subclass.delete_user) or
            NotImplemented
        )

    @abc.abstractmethod
    def get_user(self, user_id: int) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def get_users(self) -> List[User]:
        raise NotImplementedError

    @abc.abstractmethod
    def create_user(self, user: User) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def update_user(self, user: User) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_user(self, user_id: int) -> bool:
        raise NotImplementedError
