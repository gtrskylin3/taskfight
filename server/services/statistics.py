from datetime import datetime, timedelta
from typing import Dict, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from server.models.task import Task


class StatisticsService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_time_by_tag(self, period: str = "all") -> Dict[str, float]:
        """
        Get total time spent on tasks grouped by tag
        period: 'day', 'week', 'month', 'year', 'all'
        """
        # Query to get sum of time_spent grouped by tag
        stmt = select(Task.tag, func.sum(Task.time_spent)).group_by(Task.tag)
        
        # Apply date filters based on period
        if period != "all":
            now = datetime.utcnow()
            if period == "day":
                start_date = now - timedelta(days=1)
            elif period == "week":
                start_date = now - timedelta(weeks=1)
            elif period == "month":
                start_date = now - timedelta(days=30)
            elif period == "year":
                start_date = now - timedelta(days=365)
            else:
                start_date = now  # fallback
            
            stmt = stmt.where(Task.created_at >= start_date)
        
        result = await self.db_session.execute(stmt)
        rows = result.all()
        
        return {row[0]: float(row[1]) if row[1] else 0.0 for row in rows}

    async def get_completed_tasks_by_tag_and_priority(
        self, period: str = "all", priority: str = None
    ) -> Dict[str, Dict[str, int]]:
        """
        Get count of completed tasks grouped by tag and priority
        period: 'day', 'week', 'month', 'year', 'all'
        priority: 'low', 'medium', 'high', or None for all
        """
        # Base query for completed tasks
        stmt = select(Task.tag, Task.priority, func.count(Task.id))
        stmt = stmt.where(Task.is_completed == True)
        stmt = stmt.group_by(Task.tag, Task.priority)
        
        # Apply date filters based on period
        if period != "all":
            now = datetime.utcnow()
            if period == "day":
                start_date = now - timedelta(days=1)
            elif period == "week":
                start_date = now - timedelta(weeks=1)
            elif period == "month":
                start_date = now - timedelta(days=30)
            elif period == "year":
                start_date = now - timedelta(days=365)
            else:
                start_date = now  # fallback
            
            stmt = stmt.where(Task.created_at >= start_date)
        
        # Apply priority filter if specified
        if priority:
            stmt = stmt.where(Task.priority == priority)
        
        result = await self.db_session.execute(stmt)
        rows = result.all()
        
        # Organize results by tag and priority
        stats = {}
        for row in rows:
            tag, p, count = row
            if tag not in stats:
                stats[tag] = {}
            stats[tag][p] = count
        
        return stats

    async def get_total_time_spent(self, period: str = "all") -> float:
        """
        Get total time spent on all tasks
        period: 'day', 'week', 'month', 'year', 'all'
        """
        stmt = select(func.sum(Task.time_spent))
        
        if period != "all":
            now = datetime.utcnow()
            if period == "day":
                start_date = now - timedelta(days=1)
            elif period == "week":
                start_date = now - timedelta(weeks=1)
            elif period == "month":
                start_date = now - timedelta(days=30)
            elif period == "year":
                start_date = now - timedelta(days=365)
            else:
                start_date = now  # fallback
            
            stmt = stmt.where(Task.created_at >= start_date)
        
        result = await self.db_session.execute(stmt)
        total = result.scalar()
        
        return float(total) if total else 0.0

    async def get_completed_tasks_count(self, period: str = "all") -> int:
        """
        Get count of completed tasks
        period: 'day', 'week', 'month', 'year', 'all'
        """
        stmt = select(func.count(Task.id)).where(Task.is_completed == True)
        
        if period != "all":
            now = datetime.utcnow()
            if period == "day":
                start_date = now - timedelta(days=1)
            elif period == "week":
                start_date = now - timedelta(weeks=1)
            elif period == "month":
                start_date = now - timedelta(days=30)
            elif period == "year":
                start_date = now - timedelta(days=365)
            else:
                start_date = now  # fallback
            
            stmt = stmt.where(Task.created_at >= start_date)
        
        result = await self.db_session.execute(stmt)
        count = result.scalar()
        
        return count if count else 0