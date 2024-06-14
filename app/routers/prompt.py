# create all routes for prompt model:

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud
from app.database import get_db
from app.schemas.prompt import PromptCreate, PromptUpdate, Prompt
from typing import List

router = APIRouter()

@router.get("/prompt/{id}")
def read_prompt(id: int, db: Session = Depends(get_db)):
    db_prompt = crud.prompt.get_prompt(db, prompt_id=id)
    if db_prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return db_prompt


@router.get("/prompts/", response_model=List[Prompt])
def read_prompts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prompts = crud.prompt.get_prompts(db, skip=skip, limit=limit)
    return prompts

    
@router.post("/users/{user_id}/prompt", response_model=Prompt)
def create_prompt(user_id: int, prompt: PromptCreate, db: Session = Depends(get_db)):
    return crud.prompt.create_prompt(db, prompt, owner_id=user_id)
