import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://EricHuang:<password>@clustera.jhuh7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
database = cluster["database_test"] 
collection = database["collection_test"]

results = collection.find({})
for i, result in enumerate(results):
    print(f"result1-{i+1}: {result}")

results = collection.find({"_id":0})
for result in results:
    print(f"result2: {result}")

results = collection.find_one({"_id":0})
print(f"result3: {results}")

print(collection.count_documents({}))