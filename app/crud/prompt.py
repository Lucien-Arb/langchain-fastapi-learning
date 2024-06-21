# create a complete CRUD for Prompt model:

from sqlalchemy.orm import Session
from app.models.prompt import Prompt
from app.schemas.prompt import PromptCreate, PromptUpdate


def get_prompt(db: Session, prompt_id: int):
    return db.query(Prompt).filter(Prompt.id == prompt_id).first()


def get_prompts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Prompt).offset(skip).limit(limit).all()


def create_prompt(db: Session, prompt: PromptCreate, owner_id: int):
    db_prompt = Prompt(**prompt.model_dump(), owner_id=owner_id)
    db.add(db_prompt)
    db.commit()
    db.refresh(db_prompt)
    return db_prompt


def update_prompt(db: Session, prompt_id: int, prompt: PromptUpdate):
    db_prompt = db.query(Prompt).filter(Prompt.id == prompt_id).first()
    for key, value in prompt.model_dump().items():
        setattr(db_prompt, key, value)
    db.commit()
    db.refresh(db_prompt)
    return db_prompt


def delete_prompt(db: Session, prompt_id: int):
    db_prompt = db.query(Prompt).filter(Prompt.id == prompt_id).first()
    db.delete(db_prompt)
    db.commit()
    return db_prompt
