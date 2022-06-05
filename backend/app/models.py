import imp
from textwrap import indent
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
    isactive = Column(String)
    # date_instert = Column(DateTime)

class Pets(Base):
    __tablename__ = "pets"

    pet_id = Column(Integer, primary_key=True, index=True)
    pet_name = Column(String)
    # pet_owner = Column(Integer, ForeignKey("user.id"))
    comment = Column(String)


class Visit(Base):
    __tablename__ = "visit"

    id = Column(Integer, primary_key=True, index=True)
    petname = Column(String, index=True)
    # visit_date = Column(DateTime)
    # pet_id = Column(Integer, ForeignKey("pets.pet_id"))
    # doctor_id = Column(Integer, ForeignKey("user.id"))
    diagnosis = Column(String, index=True)
    drugs = Column(String)
    vaccine = Column(Boolean, default=False)