from tabnanny import check
from sqlalchemy.orm import Session

from models import Pets, User, Visit 
from schemas import UsersSchema, VisitSchema, PetSchema ,Login
# Helpfull function



from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def get_user(db:Session,skip:int=0,limit:int=100):
    return db.query(User).offset(skip).limit(limit).all()

def get_pet(db:Session,skip:int=0,limit:int=100):
    return db.query(Pets).offset(skip).limit(limit).all()

def get_visit(db:Session,skip:int=0,limit:int=100):
    return db.query(Visit).offset(skip).limit(limit).all()


# Helpfull function ************************
def get_user_by_id(db:Session,user_id:int):
    return db.query(User).filter(User.id == user_id).first()

def get_visit_by_id(db:Session,visit_id:int):
    return db.query(Visit).filter(Visit.id == visit_id).first()

def get_pet_by_id(db:Session,pet_id:int):
    return db.query(Pets).filter(Pets.id == pet_id).first()
# end Helpfull function ************************

# fuction return all user properties
def login_creds(db:Session,eml):
    return db.query(User).filter(User.email == eml).first()

# user authentication function verify if given password match to real password
def authenticate_user(db:Session,email,password):
    check = db.query(User.password).filter(User.email == email).scalar()
    if check:
        pwdchec = pwd_context.verify(password, check)
        print(pwdchec)
        return pwdchec  
    else:
        return False 

# def login_creds(db:Session,log: Login):
#     check = db.query(User.password).filter(User.email == log.email).scalar()
#     pwdchec = pwd_context.verify(log.password, check)
#     if pwdchec:
#         return db.query(User).filter(User.email == log.email).first()


# user Doctor Search Pet History visits
def get_visit_by_petname(db:Session, petname:str ):
    return db.query(Visit).filter(Visit.petname == petname).all()

# Doctor create visit
def create_visit(db: Session, visit: VisitSchema):
    _visit = Visit(id = visit.id, petname = visit.petname,diagnosis = visit.diagnosis,doctor_name = visit.doctor_name , drugs = visit.drugs,visitdate = visit.visitdate, vaccine=visit.vaccine)
    db.add(_visit)
    db.commit()
    db.refresh(_visit)
    return _visit


# function hash password
def get_password_hash(password):
    return pwd_context.hash(password)

# For all users Create an account
def create_user(db: Session, user: UsersSchema):
    _user = User(id = user.id ,address=user.address, email=user.email,isactive=user.isactive,
    password=get_password_hash(user.password),type_of_user=user.type_of_user,user_name=user.user_name)      
    db.add(_user)    
    db.commit()
    db.refresh(_user) 
    return _user

# Simple user create account for his pet
def create_pet_acc(db:Session, pet: PetSchema):
    _pet = Pets(id= pet.id, category=pet.category,pet_name=pet.pet_name,age=pet.age,owner=pet.owner,comment=pet.comment)
    db.add(_pet)
    db.commit()
    db.refresh(_pet)
    return _pet

# Simple user see pets Statistics
# TODo


# Admin delete user
def remove_user(db:Session, user_id:int):
    _user= get_user_by_id(db=db,user_id=user_id)
    db.delete(_user)
    db.commit()

# Admin delete visis
def remove_visit(db:Session, visit_id:int):
    _visit= get_visit_by_id(db=db,visit_id=visit_id)
    db.delete(_visit)
    db.commit()

def remove_pet(db:Session, pet_id:int):
    _pet= get_pet_by_id(db=db,pet_id=pet_id)
    db.delete(_pet)
    db.commit()

#todo
# Admin accept new users...change status to true....
# Show all with status false
# Update status to true
