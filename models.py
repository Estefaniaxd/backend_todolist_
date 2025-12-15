from sqlalchemy import Column, Integer, String, Float, Boolean, Date, DateTime, func, ForeignKey
from db import Base 

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(500), nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
