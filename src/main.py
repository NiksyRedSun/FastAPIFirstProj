from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate
from src.operations.router import router as router_operation
from src.pages.router import router as router_pages
from src.chat.router import router as router_chat

app = FastAPI(
    title="Trading App"
)

app.mount("/src/static", StaticFiles(directory="src/static"), name="static")


# Ниже два роутера - для аутентификации и регистрации
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

fake_traders = [
    {"id": 1, "currency": "BTC", "side": "but", "price": 123, "amount": 2.12},
    {"id": 2, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},

]

app.include_router(router_chat)
app.include_router(router_operation)
app.include_router(router_pages)
# uvicorn src.main:app --reload

