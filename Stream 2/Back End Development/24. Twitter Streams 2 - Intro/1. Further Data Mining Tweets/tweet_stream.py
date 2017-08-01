from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
 
# Replace these values with our own twitter app settings
CONSUMER_KEY = '1234xyz'
CONSUMER_SECRET = '1234xyz'
OAUTH_TOKEN = '2535164173-1234xyz'
OAUTH_TOKEN_SECRET = '1234xyz'                                                    ###

# create a keyword list of string objects to search with
keyword_list = [ 'python', 'java', 'c#', 'ruby' ] # track list

# create a child class of stream listener to pull the live data
class MyStreamListener(StreamListener):

    ###
    # override the on_data function to take stream data as a param
    # you open a file on_data() that handles:
    '''
        replies to statuses
        deletes
        events
        direct messages
        friends
        limits, disconnects and warnings
    '''
    ###
    def on_data(self, data):
        try:
            # attempt to write the stream to file and save it as a json file
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print "Failed on_data: %s" % str(e)
        return True

    # override the on error function, if we fail to connect due to failed
    # authentication or being rate limited (error code 420)
    def on_error(self, status):
        print status
        return True

# Create an instance of Tweepys  OAuthHandler class by passing in the
# CONSUMER_KEY and CONSUMER_SECRET values, and assign the instance to the
# auth variable
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

# Invoke the set_access_token function passing in the OAUTH_TOKEN and
# OAUTH_TOKEN_SECRET values as arguments The OAuthHandler object now
# has everything it needs to connect and authenticate with the new Twitter
# application you just created on the Twitter developers site
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# create an instance of the stream class and pass it an instance of
# the stream listener and the auth object
twitter_stream = Stream(auth, MyStreamListener())

# invoke the filter function object to search for and pull the stream data
# this function takes the hashtag list as its filter list (track)
twitter_stream.filter(track=keyword_list)
