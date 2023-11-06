from fastapi import APIRouter
from src.adapter.driven.infra.database.repositories.user_repository import (
    UserRepository,
)
from src.core.application.services.user_service import UserService
from src.adapter.driver.api.controllers.user_controller import (
    UserController
)

user_repository = UserRepository()
user_service = UserService(user_repository)
user_controller = UserController(user_service)


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def read_users():
    return user_controller.get_users()

