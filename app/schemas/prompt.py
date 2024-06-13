from pydantic import BaseModel

class Prompt(BaseModel):
    prompt: str

    class Config:
        orm_mode = True