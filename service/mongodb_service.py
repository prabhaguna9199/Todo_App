from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://127.0.0.1:27017/')

# create database
db = client["todo"]

# create collection
task = db["task"]


# new_task = {
# "id": "124",
#
# "task_name": "testing",
# "due_date": 2024 - 3 - 12,
# "done": "False"

# }


def create_task(task_data):
    task.insert_one(task_data)
    find_all()


def find_all():
    find_data = list(task.find({}))
    print(find_data)
    return find_data


def update_one(task_id: str, new_data: dict):
    result = task.update_one({"_id": ObjectId(task_id)}, {"$set": new_data})
    return {" task updated successfully"}
    # find_task_by_id({"_id": ObjectId(task_id)})


def Delete_task_by_id(task_id):
    result = task.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count:
        return {" task deleted successfully"}
    else:
        return {"id has not found"}


def find_task_by_id(task_id):
    return task.find_one({"_id": ObjectId(task_id)})

# def find_and_update_task_by_id(task_id, new_value: dict):
# return task.findOneAndUpdate({"_id": ObjectId(task_id)}, {"$set": new_value})
