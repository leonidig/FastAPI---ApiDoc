from fastapi import (APIRouter,
                     Depends,
                     status,
                     HTTPException)
from sqlalchemy import select

from ..schemas import CreateUser, Roles
from ..db import SESSION, User, get_session



users_router = APIRouter(prefix="/user", tags=["users"])


def get_user(email: str, session = Depends(get_session)):
    user = session.scalar(select(User).where(User.email == email))
    return user



@users_router.get("/selected_user",
                    status_code=status.HTTP_200_OK,
                    summary = "Get Selected User",
                    description = "Get selected user data by email"
                )
def select_user(email: str, session = Depends(get_session)):
    user = get_user(email, session)
    if user:
        return user
    else:
        return "No Data"



@users_router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    summary="Create New User",
    description="Creates a new user with the specified role and credentials. This route expects a user role and user data (including email and password)",
)
def create_user(role: Roles, data: CreateUser, session = Depends(get_session)) -> str:
    existing_user = get_user(data.email, session)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email already exists"
        )
    user = User(
        email=data.email,
        password=data.password,
        role=role
    )
    session.add(user)
    return "User Created"



@users_router.delete("/delete",
                     status_code=status.HTTP_200_OK,
                     summary="Delete User",
                     description="Deletes a user by email"
                     )
def delete_user(email: str, session = Depends(get_session)) -> str:
    user = get_user(email, session)
    if not user:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not Found"
        )
    session.delete(user)

    return "User deleted"
