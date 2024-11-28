import os
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


# Database URL (you should use an environment variable to store this securely)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://myuser:mypassword@localhost/postgres")

# Create a Database connection for async queries
database = Database(DATABASE_URL)

# SQLAlchemy setup
metadata = MetaData()
Base = declarative_base(metadata=metadata)

# Async engine for async queries
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# SessionLocal is for creating a session in async queries (not directly used in async operations)
# For asynchronous database operations we will use Database object from the databases library
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,  # specify AsyncSession for async operations
    expire_on_commit=False,
)

 