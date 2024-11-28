from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from database.connection import SessionLocal

# Dependency to get the database session
async def get_db():
    async with SessionLocal() as session:  # Asynchronous session
        yield session
