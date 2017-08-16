import matplotlib.pyplot as plt
'''
This line imports the integral pyplot, which we’re going to use throughout
this entire series. We import pyplot as plt, and this is a traditional
standard for python programs using pylot.
'''

'''
Next, we invoke the .plot method of pyplot to plot some coordinates.
This .plot takes many parameters, but the first two here are ‘x’ and ‘y’
coordinates, which we’ve placed lists into. This means we have 3 coordinates
according to these lists: 1,5 2,7 and 3,4.

The plt.plot will “draw” this plot in the background, but we need to bring it
to the screen when we’re ready, after graphing everything we intend to.
'''
plt.plot([1,2,3],[5,7,4])
plt.show()
