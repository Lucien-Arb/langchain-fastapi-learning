from pydantic import BaseModel, EmailStr, Field
from app.schemas.prompt import Prompt


class UserBase(BaseModel):
    username: str = Field(unique=True, max_length=255)
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    roles: list[str] = Field(default_factory=lambda: ["user"])
    is_alive: bool = True
    is_superuser: bool = False


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=40)


class UserUpdate(UserBase):
    email: EmailStr | None = Field(
        default=None, max_length=255)  # type: ignore
    password: str | None = Field(default=None, min_length=8, max_length=40)

    class Config:
        orm_mode = True


class UserInDB(UserBase):
    hashed_password: str


class User(UserBase):
    user_id: int
    prompts: list["Prompt"] = []

    class Config:
        orm_mode = True
