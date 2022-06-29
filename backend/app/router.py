from models import User
from fastapi import APIRouter, HTTPException, Path, Depends
from database import SessionLocal
from sqlalchemy.orm import Session 
from schemas import UsersSchema, RequestUser, Response, Request,RequestVisit,VisitSchema, PetSchema, Login
import crud
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta, datetime
from jose import jwt


#parameters and type of algorithm we use for jdk token
SECRET_KEY = '2db4f59778d1868f2b759f91267623a7b81575047b8cc1fc6804ac3c68bfb876'
ALGORITHM = "HS256"

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create account
@router.post("/user/createuser")
async def create(user: UsersSchema, db: Session = Depends(get_db)):
    crud.create_user(db, user = user)
    return Response(status="Ok",
                    code="200",
                    message="User account created successfully").dict(exclude_none=True)
# create pet account
@router.post("/user/createpet")
async def create(pet: PetSchema, db: Session = Depends(get_db)):
    crud.create_pet_acc(db, pet = pet)
    return Response(status="Ok",
                    code="200",
                    message="Pet acccount created successfully").dict(exclude_none=True)

# create visit
@router.post("/doctor/createvisit")
async def create(visit: VisitSchema, db: Session = Depends(get_db)):
    crud.create_visit(db, visit=visit)
    return Response(status="Ok",
                    code="200",
                    message="Visit created successfully").dict(exclude_none=True)

# create token function
# data param is the role of user and id
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
def create_access_token(data: dict, expires_delta:timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp":expire})
    encoded_jwd = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwd


@router.post("/token")
async def login(form_data:OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    eml = form_data.username
    pwd = form_data.password
    # check if username and password exist in database
    if crud.authenticate_user(db, eml, pwd):
        _creds :User
        _creds = crud.login_creds(db, eml)
        _creds.type_of_user
        print(_creds.type_of_user)
        # pass parameter of role and expire time
        access_token = create_access_token(
            data={"sub":_creds.type_of_user}, 
            expires_delta=timedelta(minutes=30)
        )
        return {"access_token":access_token, "token_type":"bearer","data":_creds} 
    else:
        raise HTTPException(status_code=400,detail="Wrong email or password")

 # example for jwt decoded

 #{
 # "sub": "user",
 # "exp": "1656524051"
 # }

# check if token is valid and return token
@router.get("/")
async def index(token: str = Depends(oauth2_scheme)):
     payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
     username: str = payload.get("sub")
     return {"token":username}  

# doctor search visit by petname and return all visits
@router.get('/doctor/search/{petname}')
async def get_all_visits(petname: str, db: Session = Depends(get_db)):
    _visit = crud.get_visit_by_petname(db, petname=petname)
    return Response(status="Ok", code="200", message="Success fetch all visit of pet data", result=_visit)

# debug function return all users
@router.get("/getallusers")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _users = crud.get_user(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users)

# debug function return all visits
@router.get("/getallvisits")
async def get_allvisits(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _users = crud.get_visit(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users)

# debug function return all pets
@router.get("/getallpets")
async def get_allpets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _users = crud.get_pet(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users)

# admin delete users
@router.delete("/deleteuser/{userid}")
async def delete(id:int, db: Session = Depends(get_db)):
    crud.remove_user(db, user_id=id)
    return Response(status="Ok",
                    code="200",
                    message="User account deleted successfully").dict(exclude_none=True)

# admin delete visit
@router.delete("/deletevisit/{visitid}")
async def delete(id:int, db: Session = Depends(get_db)):
    crud.remove_visit(db, visit_id=id)
    return Response(status="Ok",
                    code="200",
                    message="Visit deleted successfully").dict(exclude_none=True)

# admin delete pet account
@router.delete("/deletepet/{petid}")
async def delete(id:int, db: Session = Depends(get_db)):
    crud.remove_pet(db, pet_id=id)
    return Response(status="Ok",
                    code="200",
                    message="Pet account created successfully").dict(exclude_none=True)

