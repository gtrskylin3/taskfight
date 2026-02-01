from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from server.models.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    priority = Column(String(10), nullable=False)  # low, medium, high
    tag = Column(String, nullable=False)
    timer = Column(Integer, nullable=False)  # in minutes
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Fields for tracking progress
    time_spent = Column(Integer, default=0)  # in minutes
    is_completed = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)  # indicates if timer is running