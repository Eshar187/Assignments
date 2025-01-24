from sqlalchemy import Column,Integer,String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class  Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String(50))
    tasks = relationship("Task", back_populates="project")



class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(500))
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=False)
    due_date = Column(Date)
    status = Column(String(50), default="Pending")
    project = relationship("Project", back_populates="tasks")
    user = relationship("User", back_populates="tasks")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    tasks = relationship("Task", back_populates="user")

