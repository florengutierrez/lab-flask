from pymongo import MongoClient

client = MongoClient()
db = client.Flask

def insert(data, coll, database=db):
    res = database[coll].insert_one[data]
    return res.inserted_id

def read(query, coll, database=db):
    data = database[coll].find(query)
    return data