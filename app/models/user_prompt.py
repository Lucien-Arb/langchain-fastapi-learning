from sqlalchemy import Column, String, Integer, ForeignKey
from app.database import Base

class UserPrompt(Base):
    __tablename__ = "user_prompts"
    user_prompt_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    prompt_id = Column(Integer, ForeignKey("prompts.prompt_id"))
    response = Column(String)
    
    def __repr__(self):
        return f"<UserPrompt(user_id={self.user_id}, prompt_id={self.prompt_id}, response={self.response})>"