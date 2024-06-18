from typing import List
from pydantic import BaseModel, Field, EmailStr
from app.schemas.prompt import Prompt

class UserBase(BaseModel):
    first_name: str = Field(min_length=1, max_length=128)
    last_name: str = Field(min_length=1, max_length=128)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(min_length=1, max_length=128)

class UserUpdate(BaseModel):
    first_name: str = Field(min_length=1, max_length=128, default=None)
    last_name: str = Field(min_length=1, max_length=128, default=None)
    email: EmailStr = None
    password: str = Field(min_length=1, max_length=128, default=None)

    class Config:
        orm_mode = True

class User(UserBase):
    user_id: int
    prompts: List["Prompt"] = []

    class Config:
        orm_mode = True