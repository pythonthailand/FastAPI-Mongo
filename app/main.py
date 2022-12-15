from fastapi import FastAPI
from pymongo import MongoClient
from bson.objectid import ObjectId
from pydantic import BaseModel
import os
import json
from bson import json_util
app = FastAPI()

# Connect to the MongoDB database
client = MongoClient(os.environ["MONGO_URI"])
db = client.get_default_database()

# Define the data model for the items in the database
class Item(BaseModel):
    name: str
    description: str

@app.get("/")
def root():
    return {"Hello": "World"}


# Create a new item
@app.post("/items/")
async def create_item(item: Item):
    result = db.items.insert_one(item.dict())
    response = {
        "code": 201,
        "message": "item added",
        "data": {
            "item_id": json.loads(json_util.dumps(result.inserted_id))
        }
    }
    
    return response

@app.get("/items/")
async def read_all():
    items = db.items.find()
    response = {
        "code": 200,
        "message": "items found",
        "data": {
            "items": json.loads(json_util.dumps(items))
        }
    }
    return response
    


# Read an item by ID
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    print(item_id)
    item = db.items.find_one({"_id": ObjectId(item_id) })
    if item:
        response = {
        "code": 200,
        "message": "success",
        "data": {
            "item": json.loads(json_util.dumps(item))
        }
        }
        return  response
    else:
        return {
            "code": 404,
            "message": "item not found",
            "data": {}
        }

# Update an item by ID
@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    result = db.items.update_one({"_id": ObjectId(item_id)}, {"$set": item.dict()})
    if result.modified_count:
        return {
            "code": 200,
            "message": "item updated",
            "data": {}
        }
    else:
        return {
            "code": 404,
            "message": "item not found",
            "data": {}
        }

# Delete an item by ID
@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    result = db.items.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count:
        return {
            "code": 200,
            "message": "item deleted",
            "data": {}
        }
    else:
        return {
            "code": 404,
            "message": "item not found",
            "data": {}
        }
