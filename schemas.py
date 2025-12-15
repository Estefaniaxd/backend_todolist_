from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ... (Otras Clases: Producto, Usuario, etc.) ...

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime
    class Config:
        from_attributes = True
