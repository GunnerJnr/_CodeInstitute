# import our data file
from data import locations

# define a dictionary with our directions in. Each direction is a set of coordinates which,
# when added to a position, will move it in that direction. So for instance, if we're currently at (1, 1),
# moving east will result in (1+1, 1) = (2, 1). Moving west will result in (1-1, 1) = (0,1)
directions = {
    'north': (0, -1),
    'east': (1, 0),
    'south': (0, 1),
    'west': (-1, 0),
}

# set the initial starting position
position = (0, 0)

# find the name of the location by using the locations dictionary imported from data
while True:
    location = locations[position]
    print 'you are at the %s' % location

    valid_directions = {}
    # When iterating through a dictionary, it is often helpful to read both the keys(k) and values(v)
    for k, v in directions.iteritems():
        # For each direction, calculate the new position (possible_position) if we were to take that direction
        possible_position = (position[0] + v[0], position[1] + v[1])
        # check to see if this position is in the list of locations.
        # get is a method on a dictionary which will return None if that key doesn't exist
        possible_location = locations.get(possible_position)

        # If the possible location exists, we print it and add it to a dictionary which contains our valid directions.
        # We can use this later if the user decides to move there.
        # It saves us doing all those calculations again
        if possible_location:
            print 'to the %s is a %s' % (k, possible_position)
            valid_directions[k] = possible_position

    # ask the user for a direction, and use the valid_directions dictionary to move us to that position.
    # When the loop begins again, we'll be in that new position
    direction = raw_input('which direction do you want to go?\n')
    # here we check the user has entered a valid direction
    new_position = valid_directions.get(direction)
    if new_position:
        position = new_position
    else:
        print "sorry, you have entered an invalid direction!"
