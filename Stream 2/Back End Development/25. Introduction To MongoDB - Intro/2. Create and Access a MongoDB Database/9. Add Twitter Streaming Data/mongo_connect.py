import json
import pymongo
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

CONSUMER_KEY = '123abc'
CONSUMER_SECRET = '123abc'
OAUTH_TOKEN = '123abc'
OAUTH_TOKEN_SECRET = '123abc'
 
keyword_list = ['france']  # track list
 
class MyStreamListener(StreamListener):
   def __init__(self, api=None):
       self.num_tweets = 0
       self.tweet_coll = None
 
   def mongo_connect(self):
       try:
           client = pymongo.MongoClient()
           print "Mongo is connected!"
           db = client.tech_tweetsDB
           self.tweet_coll = db.tweets  # collection
       except pymongo.errors.ConnectionFailure, e:
           print "Could not connect to MongoDB: %s" % e
 
   def on_data(self, data):
       try:
 
           # read in a tweet
           status = json.loads(data)
           print json.dumps(status, indent=4)
           # create a dict to filter our preferred tweet properties
           tweet = {}
           tweet["text"] = status['text'].encode('utf-8')
           tweet['screen_name'] = status['user']['screen_name']
           tweet['followers_count'] = status['user']['followers_count']
           tweet['friends_count'] = status['user']['friends_count']
           tweet['favorite_count'] = status['favorite_count']
           tweet['retweet_count'] = status['retweet_count']
           # check if media url included in status
           print status.get('entities').get("media")
           if status.get('entities').get("media"):
               print status.get('entities').get("media")
               media = status['entities']["media"]
               tweet['media'] = media[0]["display_url"]
           else:
               tweet['media'] = None
 
           tweet['lang'] = status['user']['lang']
           tweet['location'] = status['user']['location']
 
           self.num_tweets += 1
           print  self.num_tweets
           if self.num_tweets < 10:
               # Insert tweet into the collection
               self.tweet_coll.insert(tweet)
               return True
           else:
               return False
 
           return True
       except BaseException as e:
           print "Failed on_data: %s" % str(e)
       return True
 
   def on_error(self, status):
       print status
       return True
 
 
# authenticate with the API
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
 
# create a StreamListener instance
stream = MyStreamListener()
# connect to the db
stream.mongo_connect()
 
twitter_stream = Stream(auth, stream)
# invoke the filter method to pull in the data
twitter_stream.filter(track=keyword_list)
