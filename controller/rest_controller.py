import json

from bson import json_util
from fastapi import FastAPI, HTTPException

import uvicorn

from model.pydantic_model import Task, DeleteTaskRequest, UpdateTask

from service.mongodb_service import create_task, find_all, find_task_by_id, update_one, Delete_task_by_id

app = FastAPI()


@app.post('/task/add')
def task_add(body: Task):
    create_task(body.dict())
    return {"ur task has been added"}


@app.get('/task/get/all')
def get_all():
    task_list = find_all()
    json_data_with_backslashes = json_util.dumps(task_list)
    return {"content": json.loads(json_data_with_backslashes)}


@app.put('/task/update/{task_id}')
def update_task(update_task_request: UpdateTask, task_id: str):
    existing_task = find_task_by_id(task_id)
    if existing_task:
        update_one(task_id, update_task_request.dict())
        return update_one(task_id, update_task_request.dict())
    else:
        HTTPException(status_code=404, detail="Task not found")


@app.delete('/task/delete')
def task_delete(delete_task_request: DeleteTaskRequest):
    existing_task = find_task_by_id(delete_task_request.id)
    if existing_task:
        Delete_task_by_id(delete_task_request.id)
        return {"task deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
