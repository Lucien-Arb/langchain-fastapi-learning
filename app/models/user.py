from app.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    
    prompts = relationship('Prompt', back_populates='owner')
    
    def __repr__(self):
        return f"<User(user_id={self.user_id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email})>"