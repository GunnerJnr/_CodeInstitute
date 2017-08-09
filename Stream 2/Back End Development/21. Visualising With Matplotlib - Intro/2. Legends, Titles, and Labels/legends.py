import matplotlib.pyplot as plt

# create two sets of coordinates to plot our lines
x = [1,2,3]
y = [5,7,4]
 
x2 = [1,2,3]
y2 = [10,14,12]

# plot the 2 lines and give them a label so we can clearly see which is which
plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')

# set some properties to further label our graph
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
