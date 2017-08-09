import json
import re
import pandas
import matplotlib.pyplot as plt

# store the path to the file we wish to read the data from
tweets_data_path = 'tweet_mining.json'

# create a function to read our json data file
def read_json(file_path):
    # create a list to store the data from the json file
    results = []

    # read the data from the json file line by line and store it in the list
    tweets_file = open(tweets_data_path, "r")

    # test the code to see if it has been populated
    for tweet_line in tweets_file:
        try:
            status = json.loads(tweet_line)
            results.append(status)
        except:
            continue

    # return the data 
    return results

# create a function that searches for and extracts tokens from the tweet text
# If it finds a match, it simply returns True, otherwise False
def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = tweet_text.lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False

# call our method and store the results
results = read_json(tweets_data_path)

###
# format the results in to columns of data based on:
# Text
# Language (that the tweet was written in)
# Country
###

# create a dataframe
statuses = pandas.DataFrame()

# store the text values
statuses['text'] = map(lambda status: status['text'], results)
# store the language values
statuses['lang'] = map(lambda status: status['lang'], results)
# sometimes there may not be a 'place' listed in the tweet,
# so set 'None' if not present
statuses['country'] = map(lambda status: status['place']['country'] if status['place'] != None else None, results)

# new DataFrame columns
statuses['python'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('python', status))
statuses['java'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('java', status))
statuses['c#'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('c#', status))
statuses['ruby'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('ruby', status))

# output the number of tweets where it is True that they contain our keywords
python = statuses['python'].value_counts()[True]
java = statuses['java'].value_counts()[True]
c_sharp = statuses['c#'].value_counts()[True]
ruby = statuses['ruby'].value_counts()[True]

### CHALLENGE SOLUTION ###
slices = [python, java, c_sharp, ruby]
coding_languages = ['python', 'java', 'c#', 'ruby']
colours = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels = coding_languages,
        colors = colours,
        startangle = 45,
        shadow = True,
        explode = (0.03, 0.03, 0.01, 0.02),
        autopct = '%1.1f%%')

plt.title('Comparison of popular coding languages\n')
plt.show()
