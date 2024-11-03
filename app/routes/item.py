from fastapi import (APIRouter,
                     Depends,
                     status,
                     HTTPException
                    )
from sqlalchemy import select

from ..schemas import CreateItem
from ..db import SESSION, Item, get_session



items_router = APIRouter(prefix="/item", tags=['items'])



def get_item(name: str, session = Depends(get_session)):
    item = session.scalar(select(Item).where(Item.name == name))
    return item


@items_router.get("/selected_user",
                  status_code = status.HTTP_200_OK,
                  summary = "Get Selected Item",
                  description = "Get selecred item data by items name"  
                )
def select_item(name: str, session = Depends(get_session)):
    item = get_item(name, session)
    if item: 
        return item
    else: 
        return "No data"


@items_router.post("/create",
                   status_code = status.HTTP_201_CREATED,
                   summary = "Create New Item",
                   description="Create a new item with data: name and description"
                   )
def create_item(data: CreateItem, session = Depends(get_session)) -> str:
    existing_item = get_item(data.name, session)
    if existing_item:
        raise HTTPException (
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A item with this name already exists"
        )
    item = Item(**data.model_dump())
    session.add(item)

    return "Item Created"

    
@items_router.delete("/delete",
                     status_code = status.HTTP_200_OK,
                     summary = "Item Not Found",
                     description = "Deletes item by name"  
                    )
def delete_item(name: str, session = Depends(get_session)) -> str:
    item = get_item(name, session)
    if not item:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Item Not Found"
        )
    session.delete(item)

    return "Item Delete"
