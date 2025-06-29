from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
import aioredis


class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()


engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True)

Base = declarative_base()

AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

redis = aioredis.from_url(settings.REDIS_URL, decode_responses=True)


async def get_redis():

    return redis
