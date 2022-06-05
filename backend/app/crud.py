from sqlalchemy.orm import Session

from models import User, Visit
from schemas import UsersSchema, VisitSchema

def get_user(db:Session,skip:int=0,limit:int=100):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db:Session,user_id:int):
    return db.query(User).filter(User.id == user_id).first()

def get_visit_by_petname(db:Session, petname:str ):
    return db.query(Visit).filter(Visit.petname == petname).all()

def create_visit(db: Session, visit: VisitSchema):
    _visit = Visit(id = visit.id, petname = visit.petname, diagnosis = visit.diagnosis, drugs = visit.drugs, vaccine=visit.vaccine)
    db.add(_visit)
    db.commit()
    db.refresh(_visit)
    return _visit

def create_user(db: Session, user: UsersSchema):
    _user = User(id = user.id ,address=user.address, email=user.email,isactive=user.isactive,
    password=user.password,type_of_user=user.type_of_user,user_name=user.user_name)      
    db.add(_user)    
    db.commit()
    db.refresh(_user)
    return _user

def remove_user(db:Session, user_id:int):
    _user= get_user_by_id(db=db,user_id=user_id)
    db.delete(_user)
    db.commit()
# def update_user() 6:01