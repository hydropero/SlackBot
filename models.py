from sqlalchemy import Time, Boolean, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base, engine


class Standups(Base):
    __tablename__ = "standups"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=False)
    date = Column(Date, unique=False)
    time = Column(Time, unique=False)
    do_yesterday = Column(String, unique=False)
    tech_do_yesterday = Column(String, unique=False)
    tech_type = Column(String, unique=False)
    challenge = Column(String, unique=False)
    do_today = Column(String, unique=False)
    blockers = Column(String, unique=False)

# rpgjhgpe]rhm
# r
# class Test_Table(Base):
#     __tablename__ = "testtable"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column('username', String, unique=True, index=False)
#     password = Column('password', String, unique=False, index=False)

Base.metadata.create_all(engine)