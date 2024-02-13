import os
from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, create_engine, Boolean
from sqlalchemy.orm import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

Base = declarative_base()


class role(Base):
    __tablename__ = "role"


    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False)
    permissions = Column("permissions", JSON)


    def __init__(self, id, name, permissions):
        self.id = id
        self.name = name
        self.permissions = permissions



class user(Base):
    __tablename__ = "user"


    id = Column("id", Integer, primary_key=True)
    email = Column("email", String, nullable=False)
    username = Column("username", String, nullable=False)
    registered_at = Column("registered_at", TIMESTAMP, default=datetime.utcnow)
    role_id = Column("role_id", Integer, ForeignKey(role.id))
    hashed_password = Column("hashed_password", String, nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)




    def __init__(self, id, email, username, registered_at,  role_id, hashed_password, is_active, is_superuser, is_verified):
        self.id = id
        self.email = email
        self.username = username
        self.registered_at = registered_at
        self.role_id = role_id
        self.hashed_password = hashed_password
        self.is_active = is_active
        self.is_superuser = is_superuser
        self.is_verified = is_verified



engine = create_async_engine(f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
async_session_maker = sessionmaker(engine=engine, class_=AsyncSession, expire_on_commit=False)