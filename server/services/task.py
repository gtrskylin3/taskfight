from typing import List, Optional
from server.repositories.task import TaskRepository
from server.schemes.task import TaskCreate, TaskUpdate, TaskResponse


class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    async def create_task(self, task_create: TaskCreate) -> TaskResponse:
        """Create a new task"""
        task_data = task_create.model_dump()
        db_task = await self.task_repository.create_task(task_data)
        return TaskResponse.from_orm(db_task)

    async def get_task(self, task_id: int) -> Optional[TaskResponse]:
        """Get a task by ID"""
        db_task = await self.task_repository.get_task(task_id)
        if db_task:
            return TaskResponse.from_orm(db_task)
        return None

    async def get_tasks(self, skip: int = 0, limit: int = 100) -> List[TaskResponse]:
        """Get all tasks with pagination"""
        db_tasks = await self.task_repository.get_tasks(skip, limit)
        return [TaskResponse.from_orm(task) for task in db_tasks]

    async def get_active_tasks(self, skip: int = 0, limit: int = 100) -> List[TaskResponse]:
        """Get active (non-completed) tasks with pagination"""
        db_tasks = await self.task_repository.get_active_tasks(skip, limit)
        return [TaskResponse.from_orm(task) for task in db_tasks]

    async def get_tasks_by_date(self, date: str) -> List[TaskResponse]:
        """Get tasks created on a specific date"""
        db_tasks = await self.task_repository.get_tasks_by_date(date)
        return [TaskResponse.from_orm(task) for task in db_tasks]

    async def get_tasks_by_tag(self, tag: str) -> List[TaskResponse]:
        """Get tasks filtered by tag"""
        db_tasks = await self.task_repository.get_tasks_by_tag(tag)
        return [TaskResponse.from_orm(task) for task in db_tasks]

    async def get_in_progress_tasks(self) -> List[TaskResponse]:
        """Get tasks that are in progress (time_spent > 0 and not completed)"""
        db_tasks = await self.task_repository.get_in_progress_tasks()
        return [TaskResponse.from_orm(task) for task in db_tasks]

    async def update_task(self, task_id: int, task_update: TaskUpdate) -> Optional[TaskResponse]:
        """Update a task"""
        task_data = task_update.model_dump(exclude_unset=True)
        db_task = await self.task_repository.update_task(task_id, task_data)
        if db_task:
            return TaskResponse.from_orm(db_task)
        return None

    async def delete_task(self, task_id: int) -> bool:
        """Delete a task"""
        return await self.task_repository.delete_task(task_id)

    async def start_timer(self, task_id: int) -> Optional[TaskResponse]:
        """Start the timer for a task"""
        task_data = {"is_active": True}
        db_task = await self.task_repository.update_task(task_id, task_data)
        if db_task:
            return TaskResponse.from_orm(db_task)
        return None

    async def pause_timer(self, task_id: int) -> Optional[TaskResponse]:
        """Pause the timer for a task"""
        task_data = {"is_active": False}
        db_task = await self.task_repository.update_task(task_id, task_data)
        if db_task:
            return TaskResponse.from_orm(db_task)
        return None

    async def stop_timer(self, task_id: int) -> Optional[TaskResponse]:
        """Stop the timer for a task and record progress"""
        # For now, just update the active status
        # In a real implementation, we would calculate the time spent
        task_data = {"is_active": False}
        db_task = await self.task_repository.update_task(task_id, task_data)
        if db_task:
            return TaskResponse.from_orm(db_task)
        return None

    async def complete_task(self, task_id: int) -> Optional[TaskResponse]:
        """Complete a task"""
        task_data = {"is_completed": True, "is_active": False}
        db_task = await self.task_repository.update_task(task_id, task_data)
        if db_task:
            return TaskResponse.from_orm(db_task)
        return None