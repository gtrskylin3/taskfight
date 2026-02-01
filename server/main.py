from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from server.api.routers.tasks import router as tasks_router
from server.api.routers.statistics import router as statistics_router
from server.database.db import engine
from server.models.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Cleanup on shutdown if needed


app = FastAPI(lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, configure this properly
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(tasks_router)
app.include_router(statistics_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to TaskFight API"}

if __name__ == '__main__':
    uvicorn.run('server.main:app', reload=True)