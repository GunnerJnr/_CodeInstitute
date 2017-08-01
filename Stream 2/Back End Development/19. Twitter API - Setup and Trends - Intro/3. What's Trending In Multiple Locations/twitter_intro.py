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

# Now its time to get some actual data back from your Twitter account
# Lets see what topics are trending right now in our nearest location The
# example below uses Dublin but you can change that to any location you like
# Yahoo has created an ever-increasing list of Where On Earth IDs (WOEID) used
# to identify locations on the planet Twitter uses these IDs to identify the
# place origin of its tweets

# Create a constant called BRISTOL_WOE_ID and assign it the WOEID for Bristol, Somerset
BRISTOL_WOE_ID = 13963
# Add another for London
LON_WOE_ID = 44418
# Invoke the trends_place Tweepy API method passing the BRISTOL_WOE_ID as an argument,
# and assign the results to the bristol_trends variable
bristol_trends = api.trends_place(BRISTOL_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
# Print the results to the console To make it more readable you format the data using the json.dumps method
print json.dumps(bristol_trends, indent=1)
print json.dumps(lon_trends, indent=1)

# Loop through the dub_trends results and extract the name attribute for each result and then add it
# to a set which is then assigned to the lon_trends_set variable.
dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])
# The same is done for lon_trends.
lon_trends_set = set([trend['name']
                      for trend in lon_trends[0]['trends']])
# Find trends common to both sets and return these to the common_trends
common_trends = set.intersection(dub_trends_set, lon_trends_set)
# print the results
print common_trends
