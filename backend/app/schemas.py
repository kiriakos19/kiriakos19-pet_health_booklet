from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T=TypeVar('T')

class UsersSchema(BaseModel):
    id: Optional[int]=None  
    type_of_user: Optional[str]=None
    user_name: Optional[str]=None
    email: Optional[str]=None
    address: Optional[str]=None
    password: Optional[str]=None
    isactive: Optional[str]=None

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestUser(BaseModel):
    parameter: UsersSchema = Field(...)

class VisitSchema(BaseModel):
    id: Optional[int]=None 
    petname: Optional[str]=None
    # visit_date = Column(DateTime)
    # pet_id = Column(Integer, ForeignKey("pets.pet_id"))
    # doctor_id = Column(Integer, ForeignKey("user.id"))
    diagnosis : Optional[str]=None
    drugs : Optional[str]=None
    vaccine : Optional[bool]=None
    
    class Config:
        orm_mode = True

class RequestVisit(BaseModel):
    parameter: VisitSchema = Field(...)

class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]