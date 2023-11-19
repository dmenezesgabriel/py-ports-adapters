from typing import Optional
from src.core.domain.value_objects.email import Email
from pydantic import BaseModel, ConfigDict, validator


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    email: str
    password: str

    @validator("email")
    def validate_email(cls, value):
        Email.validate(value)
        return value
