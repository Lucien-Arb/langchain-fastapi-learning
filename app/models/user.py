from app.database import Base
from sqlalchemy import Boolean, Column, String, Integer, JSON
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    roles = Column(JSON, default=lambda: ["user"])
    is_alive = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    prompts = relationship('Prompt', back_populates='owner')

    def __repr__(self):
        return f"<User(user_id={self.user_id}, first_name={self.username} , email={self.email}, roles={self.roles}, is_alive={self.is_alive}, is_superuser={self.is_superuser})>"
