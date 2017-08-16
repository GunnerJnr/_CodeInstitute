Evolving the Cells
==================

##### In this unit the students will learn how to modify the cells of Conway's Game of Life

 

The only remaining thing to do now is applying the cell life/death rules we
listed earlier. To do this, we’ll need a way to iterate through the neighbours
of each cell, and see how many are alive.

 

Luckily, we wrote something similar to this for our Boggle solver, so it should
be familiar:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_neighbours((x, y)):
    positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                 (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
    return [cells[r, c] for (r, c) in positions if 0 <= r < rows and 0 <= c < columns]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We’re just returning the neighbours of a given cell, making sure that each one
is in the grid. Now that we know the neighbours around each cell, it’s just a
case of writing
a [function](http://codeinstitute.wpengine.com/glossary/function/) to iterate
through all the cells in the grid and change
their [state](http://codeinstitute.wpengine.com/glossary/state/) accordingly:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def evolve():
    for position, alive in cells.items():
        live_neighbours = sum(get_neighbours(position))
        if alive:
            if live_neighbours not in [2, 3]:
                cells[position] = False
        elif live_neighbours == 3:
            cells[position] = True
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

**Line 2: **We iterate through the key and value of each cell dictionary entry.
So **position** is the **coordinate**, and **alive** is
a [boolean](http://codeinstitute.wpengine.com/glossary/boolean/).

 

**Line 3:** We use a trick here to get the number of live neighbours.
Python’s **sum** [function](http://codeinstitute.wpengine.com/glossary/function/) allows
us to sum a list of numbers – but True and False evaluate to 1 and 0
respectively, so **sum** in this case will return the number of live neighbours.

 

**Lines 4-8:** These are the rules introduced at the start of the lesson.
In **line 5**, we’re saying ‘if a cell doesn’t have 2 or 3 neighbours, it will
die’. We could have also written it as **if live\_neighbours \<
2** or **live\_neighbours \> 3**.

 

The program should now look like this:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import random
import sys
 
import pygame
 
from colours import dark_blue, green, black
 
 
def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, dark_blue, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, dark_blue, (0, y), (width, y))
 
 
def draw_cells():
    for (x, y) in cells:
        colour = green if cells[x, y] else black
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, colour, rectangle)
 
 
def get_neighbours((x, y)):
    positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                 (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
    return [cells[r, c] for (r, c) in positions if 0 <= r < rows and 0 <= c < columns]
 
 
def evolve():
    for position, alive in cells.items():
        live_neighbours = sum(get_neighbours(position))
        if alive:
            if live_neighbours < 2 or live_neighbours > 3:
                cells[position] = False
        elif live_neighbours == 3:
            cells[position] = True
 
 
def get_cells(density=0.2):
    return {(c, r): random.random() < density for c in range(columns) for r in range(rows)}
 
 
pygame.init()
 
columns, rows = 50, 50
cells = get_cells()
 
cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
    draw_cells()
    evolve()
    draw_grid()
    pygame.display.update()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Try running the program, and adjusting the population density. You’ll notice the
simulation is running far too fast – we need to slow it down somehow.

 

The simplest way to do this is adding a call to **time.sleep** in the game loop,
which expects the time in seconds as an argument:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
time.sleep(1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

This isn’t a particularly great way of managing the frame rate though, because
the delay will always be equal to computation time + 1 second, and computation
time might change depending on a factor such as the grid size.

 

A better way is to use PyGames built in clock:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
clock = pygame.time.Clock()
 
while True:
    clock.tick(2)
    for event in pygame.event.get():
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Instead of specifying the time to sleep, we can specify the frame rate,
so **clock.tick(2)** will make sure the frame rate is 2 frames/s.

 

### SUMMARY

In this lesson you have:

-   learned that it’s possible to create a complex system with just a small set
    of rules

-   installed PyGame

-   learned to use PyGames event system and respond to events

-   learned about random number generators

 

CHALLENGE
=========

 

-   here are many interesting patterns which have been discovered, some of which
    are
    at <https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns>.

 

-   Try and implement them in the program. For the smaller patterns, you might
    start off setting all cells to False, then adding one pixel at a time using
    cells[x,y]=True. For larger patterns it might be necessary to define them as
    a string, then convert them to cells, e.g.:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
boat = """
00000
01100
01010
00100
00000
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

-   Add some controls to the program, for instance pressing left and right could
    slow down / speed up the frame rate. You can find the key code for all the
    keys at <http://www.pygame.org/docs/ref/key.html>

 

Please Note:

 

My actual solution will follow in the near future, due to work and time
restrictions I will be rushing through the course to get the content complete
and coming back to the solutions at a later date. Thanks
