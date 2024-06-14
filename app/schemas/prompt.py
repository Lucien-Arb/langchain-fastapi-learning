from pydantic import BaseModel, Field, field_validator

class PromptBase(BaseModel):
    content: str = Field(..., min_length=1)

    @field_validator('content')
    def content_not_empty(cls, value):
        if not value.strip():
            raise ValueError('Le contenu de la prompt ne peut pas être vide')
        return value

        
class PromptCreate(PromptBase):
    pass
    
class PromptUpdate(PromptBase):
    pass

class Prompt(PromptCreate):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True