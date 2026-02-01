from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from server.database.db import get_db
from server.services.task import TaskService
from server.repositories.task import TaskRepository
from server.schemes.task import TaskCreate, TaskUpdate, TaskResponse


router = APIRouter(prefix="/tasks", tags=["tasks"])


def get_task_service(db_session: AsyncSession = Depends(get_db)):
    task_repo = TaskRepository(db_session)
    return TaskService(task_repo)


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task: TaskCreate, task_service: TaskService = Depends(get_task_service)
):
    return await task_service.create_task(task)


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int, task_service: TaskService = Depends(get_task_service)
):
    task = await task_service.get_task(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return task


@router.get("/", response_model=List[TaskResponse])
async def get_tasks(
    skip: int = 0,
    limit: int = 100,
    task_service: TaskService = Depends(get_task_service),
):
    return await task_service.get_tasks(skip=skip, limit=limit)


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task_update: TaskUpdate,
    task_service: TaskService = Depends(get_task_service),
):
    updated_task = await task_service.update_task(task_id, task_update)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return updated_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int, task_service: TaskService = Depends(get_task_service)
):
    deleted = await task_service.delete_task(task_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return


@router.get("/tag/{tag}", response_model=List[TaskResponse])
async def get_tasks_by_tag(
    tag: str, task_service: TaskService = Depends(get_task_service)
):
    return await task_service.get_tasks_by_tag(tag)


@router.get("/in-progress", response_model=List[TaskResponse])
async def get_in_progress_tasks(
    task_service: TaskService = Depends(get_task_service)
):
    return await task_service.get_in_progress_tasks()


@router.post("/{task_id}/start-timer", response_model=TaskResponse)
async def start_timer(
    task_id: int, task_service: TaskService = Depends(get_task_service)
):
    task = await task_service.start_timer(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return task


@router.post("/{task_id}/pause-timer", response_model=TaskResponse)
async def pause_timer(
    task_id: int, task_service: TaskService = Depends(get_task_service)
):
    task = await task_service.pause_timer(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return task


@router.post("/{task_id}/stop-timer", response_model=TaskResponse)
async def stop_timer(
    task_id: int, task_service: TaskService = Depends(get_task_service)
):
    task = await task_service.stop_timer(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return task


@router.post("/{task_id}/complete", response_model=TaskResponse)
async def complete_task(
    task_id: int, task_service: TaskService = Depends(get_task_service)
):
    task = await task_service.complete_task(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return task