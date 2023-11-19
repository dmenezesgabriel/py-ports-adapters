import re

from src.core.domain.base.exceptions import InvalidEmailError


class Email:
    @staticmethod
    def validate(address: str) -> None:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", address):
            raise InvalidEmailError(f"Email {address} is invalid.")
