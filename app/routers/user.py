# create all routes for user model:

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud
from app.database import get_db
from app.schemas.user import UserCreate, UserUpdate, User
from typing import List

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.user.create_user(db, user)

@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.user.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/user/")
def read_user(db: Session = Depends(get_db)):
    return "read user"
    # users = crud.get_users(db)
    # return users

