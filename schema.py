from typing import Optional
from pydantic import BaseModel

class Project(BaseModel):
    name : str
    description: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    status: Optional[str] = None

class Task(BaseModel):
    name: str
    description: Optional[str] = None
    project_id: int
    assigned_to: Optional[int] = None
    due_date: Optional[str] = None
    status: Optional[str] = None

class User(BaseModel):
    name: str
    email: str

class ProjectResponse(Project):
    id: int

    class Config:
        orm_mode = True

class TaskResponse(Task):
    id: int

    class Config:
        orm_mode = True

class UserResponse(User):
    id: int

    class Config:
        orm_mode = True


