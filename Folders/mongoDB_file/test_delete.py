import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://EricHuang:<password>@clustera.jhuh7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
database = cluster["database_test"] 
collection = database["collection_test"]

collection.delete_one({"_id": 2})
collection.delete_many({})
