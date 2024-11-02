from fastapi import APIRouter


default_router = APIRouter(prefix="/default")


@default_router.get("/", summary="Default Endpoint")
def index():
    return {"Hello" : "World!"}