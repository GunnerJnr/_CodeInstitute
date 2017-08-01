import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter
 
# Replace these values with our own twitter app settings
CONSUMER_KEY = '1234xyz'
CONSUMER_SECRET = '1234xyz'
OAUTH_TOKEN = '2535164173-1234xyz'
OAUTH_TOKEN_SECRET = '1234xyz'

# Create an instance of Tweepys  OAuthHandler class by passing in the
# CONSUMER_KEY and CONSUMER_SECRET values, and assign the instance to the
# auth variable
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

# Invoke the set_access_token function passing in the OAUTH_TOKEN and
# OAUTH_TOKEN_SECRET values as arguments The OAuthHandler object now
# has everything it needs to connect and authenticate with the new Twitter
# application you just created on the Twitter developers site
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Create an instance of the Tweepy API that will do the actual data access.
# In order for Twitter to allow the access to the API you pass in the
# OAuthHandler object when instantiating it
api = tweepy.API(auth)

count = 150
query = 'Game Development'

# get all the tweets from the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10 # the min amount of times a status is retweeted to gain entry to our list
                    # reset this value to suit your own tests

pop_tweets = [ status
               for status in results
                   if status._json['retweet_count'] > min_retweets ]

# create a list of tweet tuples associating each tweets text with its retweet count
tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
              for tweet in pop_tweets]

# sort our tuple entries in descending order
most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

# prettify and output our results
table = PrettyTable(field_names=['Text', 'Retweet Count'])

for key, val in most_popular_tups:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r' # align the columns
print table
