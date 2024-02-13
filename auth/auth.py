from fastapi_users.authentication import JWTStrategy, AuthenticationBackend
from fastapi_users.authentication import CookieTransport



# этот файл с созданием бэкенда для аутентификации
cookie_transport = CookieTransport(cookie_name='bonds', cookie_max_age=3600)

SECRET = "SECRET"


# 3600 - это период жизни кука
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)




auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)