from sqlalchemy import Column, Integer, String,DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    feedback_response = Column(String, unique=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
    
