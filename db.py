import sqlalchemy as db

# Initializes a connect with the database

with open('dbinfo') as dbinfo:
  lines = dbinfo.readlines()
  username = lines[2].split('=')[1].strip()
  password = lines[3].split('=')[1].strip()
  database = lines[4].split('=')[1].strip()


engine = db.create_engine(f'postgresql+psycopg2://{username}:{password}@127.0.0.1/{database}')