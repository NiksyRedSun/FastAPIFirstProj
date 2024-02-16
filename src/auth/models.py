from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from src.database import Base
from src.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine



class role(Base):
    __tablename__ = "role"


    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False)
    permissions = Column("permissions", JSON)


    def __init__(self, id, name, permissions):
        self.id = id
        self.name = name
        self.permissions = permissions


class User(Base):
    __tablename__ = "User"

    id = Column("id", Integer, primary_key=True)
    email = Column("email", String, nullable=False)
    username = Column("username", String, nullable=False)
    registered_at = Column("registered_at", TIMESTAMP, default=datetime.utcnow)
    role_id = Column("role_id", Integer, ForeignKey(role.id))
    hashed_password = Column("hashed_password", String, nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)



# user = User.__table__