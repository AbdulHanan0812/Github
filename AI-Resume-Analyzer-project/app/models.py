from sqlalchemy import Column, ForeignKey, Integer, String, Text

try:
    from .db import Base
except ImportError:
    from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
   
    username = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(100), nullable=False)


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
   
    resume = Column(Text, nullable=False)        
    role = Column(String(100), nullable=False)   
    result = Column(Text, nullable=False)        