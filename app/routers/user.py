# create all routes for user model:

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.authentication import RoleChecker
from .. import crud
from app.database import get_db
from app.schemas.user import UserCreate, UserUpdate, User

router = APIRouter()

tags_metadata = [
    {
        "name": "User",
        "description": "Operations with users. The **user** is the main item in the system. We have to manage them carefully.",
    },
]

# A user can read all users if they have the admin role in the user.roles list
@router.get("/users/", tags=["User"], response_model=list[User])
def read_users(_: Annotated[bool, Depends(RoleChecker(allowed_roles=["admin"]))], skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.user.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", tags=["User"], response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/", tags=["User"], response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.user.create_user(db, user)


@router.patch("/users/{id}", tags=["User"])
def update_user(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.user.update_user(db, user, user_id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/users/{user_id}", tags=["User"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.user.delete_user(db, user_id)
