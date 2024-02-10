from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, create_engine
from sqlalchemy.orm import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


engine = create_engine("sqlite:///C:\\repos\\FastAPIFirstProj\\fapi.db", echo=True)


#создание сешнемейкера
Session = sessionmaker(bind=engine)



class Roles(Base):
    __tablename__ = "Roles"


    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, nullable=False)
    permissions = Column("permissions", JSON)


    def __init__(self, id, name, permissions):
        self.id = id
        self.name = name
        self.permissions = permissions



class Users(Base):
    __tablename__ = "Users"


    id = Column("id", Integer, primary_key=True)
    email = Column("email", String, nullable=False),
    username = Column("username", String, nullable=False)
    password = Column("password", String, nullable=False)
    registered_at = Column("registered_at", TIMESTAMP, default=datetime.utcnow)
    role_id = Column("role_id", Integer, ForeignKey("Roles.id"))


    def __init__(self, id, email, username, password, registered_at, role_id):
        self.id = id
        self.email = email
        self.username = username
        self.password = password
        self.registered_at = registered_at
        self.role_id = role_id



# Base.metadata.create_all(bind=engine)


