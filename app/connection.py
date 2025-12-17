from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

# access database connection string
connection_str = os.getenv("DB_URL")

class Base(DeclarativeBase):
    pass

# create engine
engine = create_engine(connection_str, echo=True)

# connect to database
try:
    connection = engine.connect()
    print("Located and connected to database!")
    connection.close()
except Exception as e:
    print(f"An error occured: {e}")

# create session factory
DBSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = DBSession