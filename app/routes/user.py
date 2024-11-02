from fastapi import (APIRouter,
                     Depends)

from ..schemas import CreateUser, Roles
from ..db import SESSION, User
from enum import Enum

users_router = APIRouter(prefix="/user", tags=["users"])


def get_session():
    with SESSION.begin() as session:
        yield session


@users_router.post("/create", status_code=201) # I don't want to set a response_model
def create_user(role: Roles, data: CreateUser, session = Depends(get_session)):
    user = User(
        email=data.email,
        password=data.password,
        role=role
    )
    session.add(user)
    return "User Created"

