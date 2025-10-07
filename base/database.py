from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

from base import settings

engine = create_async_engine(
    url=settings.database_url,
    echo=settings.ECHO,
    pool_pre_ping=True,
)

session_maker = async_sessionmaker(engine, expire_on_commit=False)

BaseModel = declarative_base()


async def get_db() -> AsyncSession:
    async with session_maker() as session:
        yield session
