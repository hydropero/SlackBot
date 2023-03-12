import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Time, Boolean, Column, Integer, String, Float, Date, ForeignKey
# Initializes a connect with the database

with open('dbinfo') as dbinfo:
  lines = dbinfo.readlines()
  username = lines[2].split('=')[1].strip()
  password = lines[3].split('=')[1].strip()
  database = lines[4].split('=')[1].strip()

Base = declarative_base()

engine = db.create_engine(f'postgresql+psycopg2://{username}:{password}@127.0.0.1/{database}')
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Standups(Base):
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


