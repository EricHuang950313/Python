import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://EricHuang:<password>@clustera.jhuh7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
database = cluster["database_test"] 
collection = database["collection_test"]

postA = {"_id":0,"name": "Eric", "value": 100}
collection.insert_one(postA)

postB = {"_id":1,"name": "Eric", "value": 200}
postC = {"_id":2,"name": "Eric", "value": 300}
collection.insert_many([postB, postC])