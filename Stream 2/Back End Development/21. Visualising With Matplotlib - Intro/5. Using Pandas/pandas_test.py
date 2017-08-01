import datetime
import pandas
from pandas_datareader import data

# create to variables to store the start and end date times
# we wish to pull data from [ Jan 1st 2010 to Aug 22nd 2015 ]
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

# this line will pull the data for Exxon from yahoo finance
# and store it in this variable
df = data.DataReader("XOM", "yahoo", start, end)

# print the info
print df.head()


