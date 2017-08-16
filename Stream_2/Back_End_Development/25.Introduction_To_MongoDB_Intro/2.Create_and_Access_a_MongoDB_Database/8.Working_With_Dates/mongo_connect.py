import pymongo
import datetime
from datetime import timedelta

def mongo_connect():
    try:
        connection = pymongo.MongoClient()
        print "MongoDB is connected!"
        return connection
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDB: %s" % e

connection = mongo_connect()
db = connection['twitter_stream']
coll = db.my_collection
coll.drop()  # remove the collection to avoid duplicates when testing
docs = [{"name": "Dave", "surname": "Gunner", "twitter": "@gunnerjnr84",
        "date": datetime.datetime.utcnow()},
       {"name": "Stephen", "surname": "Fry", "twitter": "@stephenfry",
        "date": datetime.datetime.utcnow() - timedelta(days=2)},
       {"name": "Stephen", "surname": "Dedalus", "twitter": "@stephend",
        "date": datetime.datetime.utcnow() + timedelta(days=10)},
       {"name": "Armand", "surname": "Tanzarian", "twitter": "@armandt",
        "date": datetime.datetime.utcnow() - timedelta(days=10), "_id": "22"}]
coll.insert_many(docs)
date = datetime.datetime.utcnow()
for doc in coll.find({"date": {"$lt": date}}).sort("name"):  # see  also -  $lte, $gte, $ne
   print doc
