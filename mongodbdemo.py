import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017")

print(db.list_database_names())
mydb = db["demo"]
x = mydb.list_collection_names()
print(x)

mytable=mydb["employee"]
a={"stuid": 8, "Name": "MNO", "salary": 66000}
print(mytable.insert_one(a))