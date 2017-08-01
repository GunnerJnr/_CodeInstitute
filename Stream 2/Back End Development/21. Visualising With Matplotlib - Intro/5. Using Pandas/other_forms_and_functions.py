import pandas
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

# create a dictionary
web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

# turn the dictionary into a dataframe
df = pandas.DataFrame(web_stats)

#print the results
print df.head()

# we can also print the last few lines using
print df.tail()

# we can even specify how many to print
print df.tail(2)

# we can also set the index number to something specific, in this case 'Day'
df.set_index('Day', inplace=True)

# plot our results
print df['Visitors']

# and print our results
print df.Visitors

# we can also plot a single column
df['Visitors'].plot()
plt.show()

# we can also plot the entire dataframe, as long as that data is normalised
# or on the same scale
df.plot()
plt.show()

# we can also reference multiple columns at a time, like so
# (we only have 2 columns, but the same works with however many you start with):
print df[['Visitors', 'Bounce Rate']]




