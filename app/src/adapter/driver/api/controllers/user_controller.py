from src.core.application.ports.user_service import UserServiceInterface


class UserController:
    def __init__(
            self,
            # logger: LoggerInterface,
            user_service: UserServiceInterface
    ):
        # self.logger = logger
        self.user_service = user_service

    def get_by_id(self):
        user = self.user_service.get_by_id()
        return user

    def get_all(self):
        users = self.user_service.get_all()
        return users

    def create(self):
        user = self.user_service.create()
        return user

    def update(self):
        user = self.user_service.update()
        return user

    def delete(self):
        user = self.user_service.delete()
        return user
