from fastapi import FastAPI, Depends, HTTPException
from model.employee import Employee
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker, Session
from database.dependencies import get_db
from sqlalchemy import MetaData, inspect

app = FastAPI()

@app.get("/employees")
async def get_employees(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Employee))  # Query for all employees
    employees = result.scalars().all()  # Get the actual employee records
    return employees
