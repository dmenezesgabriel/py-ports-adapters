import pydantic


@pydantic.dataclasses.dataclass
class User():
    email: str
    password: str
