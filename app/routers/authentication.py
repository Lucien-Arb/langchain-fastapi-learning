# create all routes for token, authentication model:

from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from sqlalchemy.orm import Session
from .. import crud
from app.database import get_db
from app.schemas.token import Token, TokenData
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from app.crud.authentication import create_access_token, get_current_active_user, ACCESS_TOKEN_EXPIRE_MINUTES
from app.schemas.user import User

router = APIRouter()

tags_metadata = [
    {
        "name": "Token",
        "description": "Operations with tokens. The **token** is the main item in the system. We have to manage them carefully.",
    },
]



@router.post("/token", tags=["Token"], response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)
) -> Token:
    user = crud.authentication.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me/", tags=["User"], response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@router.get("/users/me/items/",tags=["User"])
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]