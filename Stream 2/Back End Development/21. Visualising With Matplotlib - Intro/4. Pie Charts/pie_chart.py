import matplotlib.pyplot as plt

# sets the relevant sizes for the pie slices
slices = [7,2,2,13]
# set the different activities each slice represents
activities = ['sleeping','eating','working','playing']
# set the colours we wish to use for the slices
cols = ['c','m','r','b']

# now we plot the pie slices and feed it the properties
plt.pie(slices,
        labels=activities,  # set the slice labels
        colors=cols,        # set the colours
        startangle=90,      # set the starting angle
        shadow= True,       # do we want shadows
        explode=(0,0.1,0,0),    # make the slice poke out a bit
        autopct='%1.1f%%')      # overlay the % on each slice (optional)

# set the pie chart title
plt.title('Interesting Graph\nCheck it out')

# show the pie chart
plt.show()
