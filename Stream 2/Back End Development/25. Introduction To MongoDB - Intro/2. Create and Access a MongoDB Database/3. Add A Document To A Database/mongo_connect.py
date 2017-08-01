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
doc = {"name": "David", "surname": "Gunner", "twitter": "@gunnerjnr84"}
coll.insert(doc)
result = coll.find_one()
print result # {u'twitter': u'@gunnerjnr84', u'_id': ObjectId('5629264db1bae125ac446ba5'), u'surname': u'Gunner', u'name': u'Dave'}
