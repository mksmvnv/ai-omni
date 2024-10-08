from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from utils.config import settings


engine = create_async_engine(settings.pg_url, echo=True)

session_marker = async_sessionmaker(engine, expire_on_commit=False)


class BaseModel(AsyncAttrs, DeclarativeBase):
    pass


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
