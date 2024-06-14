from pydantic import BaseModel, Field, EmailStr
from app.schemas.prompt import Prompt

class UserBase(BaseModel):
    user_id: int
    first_name: str = Field(min_length=1, max_length=128)
    last_name: str = Field(min_length=1, max_length=128)
    email: EmailStr
    password: str = Field(min_length=1, max_length=128)
        
        
class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    user_id: int
    first_name: str = Field(min_length=1, max_length=128)
    last_name: str = Field(min_length=1, max_length=128)
    email: EmailStr
    password: str = Field(min_length=1, max_length=128)


class User(UserCreate):
    user_id: int
    prompts: list[Prompt] = []
    
    class Config:
        orm_mode = True
    