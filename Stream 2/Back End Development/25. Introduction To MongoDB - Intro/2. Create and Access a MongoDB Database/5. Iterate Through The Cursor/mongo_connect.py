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
coll.drop()  # remove the collection
docs = [{"name": "Dave", "surname": "Gunner", "twitter": "@gunnerjnr84"},
       {"name": "Stephen", "surname": "Fry", "twitter": "@stephenfry"},
       {"name": "Dave", "surname": "Gunner", "twitter": "@gunnerjnr84"}]
coll.insert_many(docs)
results = coll.find()
for doc in results:
   print doc
