from enum import Enum
from pydantic import BaseModel


class Roles(str, Enum):
    ADMIN = "admin"
    USER = "user"


class CreateUser(BaseModel):
    email: str
    password: str

