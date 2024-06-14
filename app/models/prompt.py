from app.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Prompt(Base):
    __tablename__ = "prompts"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey('users.user_id'))
    
    owner = relationship('User', back_populates='prompts')
    
    def __repr__(self):
        return f"<Prompt(prompt_id={self.id}, prompt={self.content})>"