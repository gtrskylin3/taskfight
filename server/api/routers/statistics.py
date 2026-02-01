from fastapi import APIRouter, Depends, Query
from typing import Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession

from server.database.db import get_db
from server.services.statistics import StatisticsService


router = APIRouter(prefix="/statistics", tags=["statistics"])


def get_statistics_service(db_session: AsyncSession = Depends(get_db)):
    return StatisticsService(db_session)


@router.get("/time-by-tag", response_model=Dict[str, float])
async def get_time_by_tag(
    period: str = Query("all", pattern="^(day|week|month|year|all)$"),
    statistics_service: StatisticsService = Depends(get_statistics_service),
):
    return await statistics_service.get_time_by_tag(period)


@router.get("/completed-tasks-by-tag-priority", response_model=Dict[str, Dict[str, int]])
async def get_completed_tasks_by_tag_and_priority(
    period: str = Query("all", pattern="^(day|week|month|year|all)$"),
    priority: str = Query(None, pattern="^(low|medium|high)$"),
    statistics_service: StatisticsService = Depends(get_statistics_service),
):
    return await statistics_service.get_completed_tasks_by_tag_and_priority(
        period, priority
    )


@router.get("/total-time-spent", response_model=float)
async def get_total_time_spent(
    period: str = Query("all", pattern="^(day|week|month|year|all)$"),
    statistics_service: StatisticsService = Depends(get_statistics_service),
):
    return await statistics_service.get_total_time_spent(period)


@router.get("/completed-tasks-count", response_model=int)
async def get_completed_tasks_count(
    period: str = Query("all", pattern="^(day|week|month|year|all)$"),
    statistics_service: StatisticsService = Depends(get_statistics_service),
):
    return await statistics_service.get_completed_tasks_count(period)