# create all routes for prompt model:

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud
from app.database import get_db
from app.schemas.prompt import PromptCreate, PromptUpdate, Prompt

router = APIRouter()

tags_metadata = [
    {
        "name": "Prompt",
        "description": "Operations with prompts. The **prompt** is the main item in the system. We have to manage them carefully.",
        "externalDocs": {
            "description": "LangChain Prompt services",
            "url": "https://python.langchain.com/v0.2/docs/introduction/",
        },
    },
]



@router.get("/prompts/", tags=["Prompt"], response_model=list[Prompt])
def read_prompts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prompts = crud.prompt.get_prompts(db, skip=skip, limit=limit)
    return prompts


@router.get("/prompt/{id}", tags=["Prompt"], response_model=Prompt)
def read_prompt(id: int, db: Session = Depends(get_db)):
    db_prompt = crud.prompt.get_prompt(db, prompt_id=id)
    if db_prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return db_prompt


@router.post("/prompt/", tags=["Prompt"], response_model=Prompt)
def create_prompt(prompt: PromptCreate, db: Session = Depends(get_db)):
    return crud.prompt.create_prompt(db, prompt)


@router.patch("/prompt/{id}", tags=["Prompt"])
def update_user(id: int, prompt: PromptUpdate, db: Session = Depends(get_db)):
    db_prompt = crud.prompt.update_prompt(db, prompt, user_id=id)
    if db_prompt is None:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return db_prompt


@router.delete("/prompt/{prompt_id}", tags=["Prompt"])
def delete_user(prompt_id: int, db: Session = Depends(get_db)):
    return crud.prompt.delete_prompt(db, prompt_id)
