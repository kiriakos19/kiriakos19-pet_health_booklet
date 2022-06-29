from datetime import datetime
import imp
from textwrap import indent
from psycopg2 import Date
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    type_of_user = Column(String)
    user_name = Column(String)
    email = Column(String)
    address = Column(String)
    password = Column(String)
    isactive = Column(Boolean, default=False)
    

class Pets(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    pet_name = Column(String)
    age = Column(Integer)
    owner = Column(String)
    comment = Column(String)


class Visit(Base):
    __tablename__ = "visit"

    id = Column(Integer, primary_key=True, index=True)
    petname = Column(String, index=True)
    visitdate = Column(String)
    doctor_name = Column(String)
    diagnosis = Column(String, index=True)
    drugs = Column(String)
    vaccine = Column(Boolean, default=False)

