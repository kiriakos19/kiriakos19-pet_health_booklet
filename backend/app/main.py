import re
from fastapi import FastAPI
import  models
from database import engine
import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, HTTPException, Path, Depends

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# @app.post("/token")
# async def token(form_data: OAuth2PasswordRequestForm = Depends()):
#     return {"access_token": form_data.username+ 'token'}

# @app.get('/')
# async def index(token: str = Depends(oauth2_scheme)):
#     return {"token":token}  

# ROUTER
app.include_router(router.router, tags=["user"])















# from typing import List
# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.future import select
# from sqlalchemy.ext.asyncio import AsyncSession

# from database import get_session, init_db
# from schemas import Users,CreateUsers

# from sqlalchemy.orm import Session
# from pydantic import BaseSettings 



# import  models 
# import schemas
# import crud
# from database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)


# app = FastAPI()


# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.on_event("startup")
# async def on_startup():
#     await init_db()


# @app.get("/ping")
# async def pong():
#     return {"ping": "pong!"}


# # @app.post("/adduser/", response_model=schemas.UserCreate)
# # def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
# #     return crud.create_user(db=db, user=user)

# @app.post("/songs")
# async def add_song(user: CreateUsers, session: AsyncSession = Depends(get_session)):
#     user = Users(id=user.id, type_of_user=user.type_of_user, user_name=user.user_name, address=user.address, password=user.password, is_active=user.is_active)
#     session.add(user)
#     await session.commit()
#     await session.refresh(user)
#     return user