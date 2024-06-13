

class UserPrompt(BaseModel):
    user_id: int
    prompt_id: int
    response: str

    class Config:
        orm_mode = True