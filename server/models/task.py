from sqlalchemy import Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from server.models.base import Base
from typing import Optional
from datetime import datetime


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    priority: Mapped[str] = mapped_column(String(10), nullable=False)  # low, medium, high
    tag: Mapped[str] = mapped_column(String, nullable=False)
    timer: Mapped[int] = mapped_column(Integer, nullable=False)  # in minutes
    created_at: Mapped[Optional[DateTime]] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[Optional[DateTime]] = mapped_column(DateTime(timezone=True), onupdate=func.now())

    # Fields for tracking progress
    time_spent: Mapped[int] = mapped_column(Integer, default=0)  # in minutes
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)  # indicates if timer is running
    timer_started_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))  # when the timer was started