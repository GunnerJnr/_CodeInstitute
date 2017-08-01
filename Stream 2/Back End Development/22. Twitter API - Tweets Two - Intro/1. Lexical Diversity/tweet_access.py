import json
import tweepy
from tweepy import OAuthHandler
 
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

count = 50
query = 'Game Development'

# Get all the tweets for the given search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [ status._json['text'] for status in results ]

screen_names = [ status._json['user']['screen_name']
                 for status in results
                 for mention in status._json['entities']['user_mentions']]

hashtags = [ hashtag['text']
             for status in results
             for hashtag in status._json['entities']['hashtags']]

words = [ word
          for text in status_texts
          for word in text.split()]


# create a function to return the average num of words
# in the text entity of a tweet
def get_lexical_diversity(items):
    return 1.0*len(set(items))/len(items)

# create a function that calculates the lexocal diversity
# of a list of text items
def get_average_words(tweets):
    total_words = sum([ len(tweet.split()) for tweet in tweets ])
    return 1.0*total_words/len(tweets)

# print the results returned by our functions
print "Average words: %s" % get_average_words(status_texts)  
print "Word Diversity: %s" % get_lexical_diversity(words)
print "Screen Name Diversity: %s" % get_lexical_diversity(screen_names)
print "HashTag Diversity: %s" % get_lexical_diversity(hashtags)

