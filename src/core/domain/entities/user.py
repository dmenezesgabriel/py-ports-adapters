from typing import Union
from src.core.domain.value_objects.email import Email
from pydantic import BaseModel, EmailStr, ConfigDict, validator


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Union[int, None] = None
    email: EmailStr
    password: str

    @validator("email")
    def validate_email(cls, email):
        Email.validate(email)
        return email
