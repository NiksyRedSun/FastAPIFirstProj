from datetime import datetime
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from models.models import role

# этот файл с созданием моделей таблиц для аутентификации

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base: DeclarativeMeta = declarative_base()


# Обрати внимание, чтобы все работало окей - эта таблица должна соответствовать той таблице, которая имеется в models
# Если хочешь, можешь добавить сюда пользовательские поля, если нужно посмотреть обязательные - то посмотри, от чего наследуются
class User(SQLAlchemyBaseUserTable[int], Base):


    id = Column("id", Integer, primary_key=True)
    email = Column("email", String, nullable=False)
    username = Column("username", String, nullable=False)
    registered_at = Column("registered_at", TIMESTAMP, default=datetime.utcnow)
    role_id = Column("role_id", Integer, ForeignKey(role.id))
    hashed_password = Column("hashed_password", String, nullable=False)
    is_active: bool = Column("is_active", Boolean, default=True, nullable=False)
    is_superuser: bool = Column("is_superuser", Boolean, default=False, nullable=False)
    is_verified: bool = Column("is_verified", Boolean, default=False, nullable=False)



engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Вот эта функция не нужна нам, поскольку таблицы мы создаем с помощью миграций
# async def create_db_and_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
