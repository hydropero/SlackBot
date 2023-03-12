import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# Initializes a connect with the database

with open('dbinfo') as dbinfo:
  lines = dbinfo.readlines()
  username = lines[2].split('=')[1].strip()
  password = lines[3].split('=')[1].strip()
  database = lines[4].split('=')[1].strip()

Base = declarative_base()

engine = db.create_engine(f'postgresql+psycopg2://{username}:{password}@127.0.0.1/{database}')
sf = sessionmaker(autocommit=False, autoflush=False, bind=engine)
