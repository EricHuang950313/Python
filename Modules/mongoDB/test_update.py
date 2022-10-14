import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://EricHuang:<password>@clustera.jhuh7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
database = cluster["database_test"] 
collection = database["collection_test"]

collection.update_one({"_id": 2}, {"$set":{"value":0}})