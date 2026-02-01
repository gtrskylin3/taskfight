from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    name: str
    priority: str  # low, medium, high
    tag: str
    timer: int  # in minutes


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    name: Optional[str] = None
    priority: Optional[str] = None  # low, medium, high
    tag: Optional[str] = None
    timer: Optional[int] = None  # in minutes
    time_spent: Optional[int] = None
    is_completed: Optional[bool] = None
    is_active: Optional[bool] = None


class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    time_spent: int = 0
    is_completed: bool = False
    is_active: bool = False

    class Config:
        from_attributes = True