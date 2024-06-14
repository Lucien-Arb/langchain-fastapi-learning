# create all routes for prompt model:

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud
from app.database import get_db
from app.schemas.prompt import PromptCreate, PromptUpdate, Prompt
from typing import List

router = APIRouter()

@router.post("/users/{user_id}/prompt", response_model=Prompt)
def create_prompt(user_id: int, prompt: PromptCreate, db: Session = Depends(get_db)):
    return crud.prompt.create_prompt(db, prompt, owner_id=user_id)

@router.get("/prompts/", response_model=List[Prompt])
def read_prompts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prompts = crud.prompt.get_prompts(db, skip=skip, limit=limit)
    return prompts

@router.get("/prompt/") #response_model=List[Prompt]
def read_prompt(db: Session = Depends(get_db)):
    return "read prompt"
    # prompts = crud.get_prompts(db)
    # return prompts

