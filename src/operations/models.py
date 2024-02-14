from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

from src.database import Base



class operation(Base):
    __tablename__ = "operation"

    id = Column("id", Integer, primary_key=True)
    quantity = Column("quantity", String)
    figi = Column("figi", String)
    instrument_type = Column("instrument_type", String, nullable=True)
    date = Column("date", String, nullable=True)
    type = Column("type", String)
