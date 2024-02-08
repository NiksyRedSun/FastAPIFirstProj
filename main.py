from fastapi import FastAPI



app = FastAPI(
    title="Trading App"
)


fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


# Включение параметров пути
@app.get("/users/{user_id}")
def hello_world(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]

fake_traders = [
    {"id": 1, "currency": "BTC", "side": "but", "price": 123, "amount": 2.12},
    {"id": 2, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},

]


# Включение параметров запроса
# через равно - значения по умолчанию
@app.get("/trades")
def hello_world(limit: int = 10, offset: int = 10):
    return fake_traders[offset:][:limit]



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


# uvicorn main:app --reload
