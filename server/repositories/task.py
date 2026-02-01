from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from server.models.task import Task


class TaskRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_task(self, task_data: dict):
        """Create a new task"""
        db_task = Task(**task_data)
        self.db_session.add(db_task)
        await self.db_session.commit()
        await self.db_session.refresh(db_task)
        return db_task

    async def get_task(self, task_id: int):
        """Get a task by ID"""
        result = await self.db_session.execute(select(Task).filter(Task.id == task_id))
        return result.scalar_one_or_none()

    async def get_tasks(self, skip: int = 0, limit: int = 100):
        """Get all tasks with pagination"""
        result = await self.db_session.execute(select(Task).offset(skip).limit(limit))
        return result.scalars().all()

    async def get_tasks_by_date(self, date: str):
        """Get tasks created on a specific date"""
        result = await self.db_session.execute(
            select(Task).filter(Task.created_at.like(f"{date}%"))
        )
        return result.scalars().all()

    async def get_tasks_by_tag(self, tag: str):
        """Get tasks filtered by tag"""
        result = await self.db_session.execute(select(Task).filter(Task.tag == tag))
        return result.scalars().all()

    async def get_in_progress_tasks(self):
        """Get tasks that are in progress (time_spent > 0 and not completed)"""
        result = await self.db_session.execute(
            select(Task).filter(Task.time_spent > 0).filter(Task.is_completed == False)
        )
        return result.scalars().all()

    async def update_task(self, task_id: int, task_data: dict):
        """Update a task"""
        stmt = update(Task).where(Task.id == task_id).values(**task_data)
        await self.db_session.execute(stmt)
        await self.db_session.commit()
        
        # Return updated task
        return await self.get_task(task_id)

    async def delete_task(self, task_id: int):
        """Delete a task"""
        stmt = delete(Task).where(Task.id == task_id)
        await self.db_session.execute(stmt)
        await self.db_session.commit()
        return True