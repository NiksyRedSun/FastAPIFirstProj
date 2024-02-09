from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Trading App"
)


fake_users = [
    {"id": 1, "role": "admin", "name": ["Bob"]},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
    {"id": 4, "role": "investor", "name": "Homer", "degree": [
        {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
    ]},
]


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"



class Degree(BaseModel):
    id: int
    created_at: datetime
    # вот тут, позволяет валидировать пользовательские типы
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    # Опционально, значит по умолчанию, можно не ставить равно и не добавлять список, тогда будет none
    degree: Optional[List[Degree]] = []

# Включение параметров пути
# response_model - указание того, каким должен быть ответ сервера (валидация отправляемых данных)
@app.get("/users/{user_id}", response_model=List[User])
def hello_world(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]




fake_traders = [
    {"id": 1, "currency": "BTC", "side": "but", "price": 123, "amount": 2.12},
    {"id": 2, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},

]


# Включение параметров запроса
# через равно - значения по умолчанию
# @app.get("/trades")
# def hello_world(limit: int = 10, offset: int = 10):
#     return fake_traders[offset:][:limit]



fake_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))
    current_user[0]['name'] = new_name
    return {"status": 200, "data": current_user}


fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
]




# Мы используем пайдентик для создания различных моделей, потому что это достаточно популярная практика,
# плюс названная выше библиотека встроена в fastapi
class Trade(BaseModel):
    id: int
    user_id: int
    # Здесь задаем максимальную длину
    currency: str = Field(max_length=5)
    side: str
    # Позволяет создать ограничения для отправляемых значений, в данном случае значения должны быть больше нуля
    price: float = Field(ge=0)
    amount: float



# С помощью аннотации типов, происходит валидация данных, получаемых сервером
@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}


# uvicorn main:app --reload
