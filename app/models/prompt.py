from sqlalchemy import Column, String, Integer
from app.database import Base


class Prompt(Base):
    __tablename__ = "prompts"
    prompt_id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String)
    
    def __repr__(self):
        return f"<Prompt(prompt_id={self.prompt_id}, prompt={self.prompt})>"