from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

#connection string 
DATABASE_URL = os.environ.get("DATABASE_URL",'postgresql://dbuser:pass123@db/test_db')
#DATABASE_URL = os.environ.get("DATABASE_URL",'postgresql://dbuser:pass123@db-postgresql:5432/test_db')

engine=create_engine(
    DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

