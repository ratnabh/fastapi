from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# This is the base class for all models
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'  # The name of the table in the database
    
    # Define the columns of the table
    id = Column(Integer, primary_key=True, index=True)  # 'id' column (primary key)
    salary = Column(Integer)  # 'salary' column

    def __repr__(self):
        return f"<Employee(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, position={self.position})>"
