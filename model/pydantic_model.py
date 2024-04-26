from typing import Optional

from pydantic import BaseModel, Field


# from datetime import datetime


class Task(BaseModel):
    task_id: str = Field(..., max_length=100)
    task_name: str = Field(..., max_length=100)
    due_date = str
    done: bool


class UpdateTask(BaseModel):
    # id: str
    # task_id: Optional[str] = None
    task_name: Optional[str] = None
    due_date: Optional[str] = None
    done: Optional[bool] = None


class DeleteTaskRequest(BaseModel):
    id: str
