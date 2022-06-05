from fastapi import APIRouter, HTTPException, Path, Depends
from database import SessionLocal
from sqlalchemy.orm import Session 
from schemas import UsersSchema, RequestUser, Response, Request,RequestVisit,VisitSchema
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def create(user: UsersSchema, db: Session = Depends(get_db)):
    crud.create_user(db, user = user)
    return Response(status="Ok",
                    code="200",
                    message="user created successfully").dict(exclude_none=True)

@router.post("/createvisit")
async def create(visit: VisitSchema, db: Session = Depends(get_db)):
    crud.create_visit(db, visit=visit)
    return Response(status="Ok",
                    code="200",
                    message="visit created successfully").dict(exclude_none=True)



@router.get("/")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _users = crud.get_user(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users)


## login user

# na dexete san orisma to anagnoristiko tou katoikidiou kai na epistrefei
# kathe mia episkepsi pou exei kanei , lista..

@router.get('/pet_name/{petname}')
async def get_all_visits(petname: str, db: Session = Depends(get_db)):
    _visit = crud.get_visit_by_petname(db, petname=petname)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_visit)

