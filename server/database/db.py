from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from server.config import settings
engine = create_async_engine(url=settings.DB_URL)

session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_db():
    async with session_maker() as session:
        yield session 
    