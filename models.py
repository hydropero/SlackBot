from sqlalchemy import Time, Boolean, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base, engine

class Test_Table(Base):
    __tablename__ = "testtable"
    id = Column(Integer, primary_key=True, index=True)
    username = Column('username', String, unique=True, index=False)
    password = Column('password', String, unique=False, index=False)

Base.metadata.create_all(engine)