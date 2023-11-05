from core.application.ports.user_service import UserServiceInterface


class UserController:
    def __init__(self, logger: LoggerInterface, user_service: UserServiceInterface):
        self.logger = logger
        self.user_service = user_service

    def get_user(self):
        user = self.user_service.get_user()
        return user

    def get_users(self):
        users = self.user_service.get_users()
        return users

    def create_user(self):
        user = self.user_service.create_user()
        return user

    def update_user(self):
        user = self.user_service.update_user()
        return user

    def delete_user(self):
        user = self.user_service.delete_user()
        return user
