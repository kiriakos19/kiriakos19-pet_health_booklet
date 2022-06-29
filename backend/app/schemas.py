from datetime import datetime
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
    isactive: Optional[bool]=None

    class Config:
        orm_mode = True

class PetSchema(BaseModel):
    id: Optional[int]=None  
    category: Optional[str]=None
    pet_name: Optional[str]=None
    age: Optional[int]=None
    owner: Optional[int]=None
    comment: Optional[str]=None
    
    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestUser(BaseModel):
    parameter: UsersSchema = Field(...)

class VisitSchema(BaseModel):
    id: Optional[int]=None 
    petname: Optional[str]=None    
    diagnosis : Optional[str]=None   
    doctor_name: Optional[str]=None    
    drugs : Optional[str]=None
    visitdate : Optional[str]=None
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
    token:Optional[str]




class Login(BaseModel):
    email:str
    password:str





