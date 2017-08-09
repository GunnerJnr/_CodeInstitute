import json
import pandas
import matplotlib.pyplot as plt

# store the path to the file we wish to read the data from
tweets_data_path = 'tweet_mining.json'

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

# print the data 
print len(results)

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

# get each tweet language and the count of its appearance (not to be confused with programming languages)
tweets_by_lang = statuses['lang'].value_counts()

# get each tweet country of origin and the count of its appearence
tweets_by_country = statuses['country'].value_counts()

# create our drawing space/window (figure)
fig = plt.figure()

# add a plot area for our data on the figure - 1,1,1 means a single chart/graph
# prepare to plot two charts on the same figure
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
 
#style the axes and labels of our plot
ax1.tick_params(axis='x', labelsize=15)
ax1.tick_params(axis='y', labelsize=10)
ax1.set_xlabel('Tweet Languages', fontsize=15)
ax1.set_ylabel('Num of Tweets' , fontsize=15)
ax1.xaxis.label.set_color('#666666')
ax1.yaxis.label.set_color('#666666')
ax1.tick_params(axis='x', colors='#666666')
ax1.tick_params(axis='y', colors='#666666')

#style the title
ax1.set_title('Top 10 languages', fontsize=15, color='#666666')
 
# plot the top 10 tweet languages and appearance count using a bar chart
tweets_by_lang[:10].plot(ax=ax1, kind='bar', color='#FF7A00')
 
# color the spines (borders)
for spine in ax1.spines.values():
        spine.set_edgecolor('#666666')

# Second subplot
ax2.tick_params(axis='x', labelsize=15)
ax2.tick_params(axis='y', labelsize=10)
ax2.set_xlabel('Countries', fontsize=15)
ax2.set_ylabel('Number of tweets' , fontsize=15)
ax2.xaxis.label.set_color('#666666')
ax2.yaxis.label.set_color('#666666')
ax2.tick_params(axis='x', colors='#666666')
ax2.tick_params(axis='y', colors='#666666')
#style the title
ax2.set_title('Top 10 Countries', fontsize=15, color='#666666')
 
# plot the top 10 tweet languages and appearance count using a bar chart
tweets_by_country[:10].plot(ax=ax2, kind='bar', color='#FF7A00')
 
# color the spines (borders)
for spine in ax2.spines.values():
        spine.set_edgecolor('#666666')
 
# render the graph
plt.show()
