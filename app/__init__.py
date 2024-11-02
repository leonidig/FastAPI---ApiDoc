from fastapi import (FastAPI,
                     APIRouter
                )


app = FastAPI(debug=True)


from .routes import (default_router,
                     users_router,
                     items_router)


app.include_router(default_router)
app.include_router(users_router)
app.include_router(items_router)