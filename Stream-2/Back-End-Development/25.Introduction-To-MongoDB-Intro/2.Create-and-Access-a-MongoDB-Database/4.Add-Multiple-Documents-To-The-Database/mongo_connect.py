import pymongo

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
docs = [{"name": "Henry", "surname": "Moore", "twitter": "@henrymoore"},
       {"name": "Stephen", "surname": "Fry", "twitter": "@stephenfry"}]
coll.insert_many(docs)
results = coll.find()
print results #<pymongo.cursor.Cursor object at 0x02909C90>
