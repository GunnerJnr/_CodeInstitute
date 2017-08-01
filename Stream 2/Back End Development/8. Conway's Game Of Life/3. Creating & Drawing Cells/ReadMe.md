Creating and Drawing Cells
==========================

##### In this unit the students will learn how to draw cells using in Conway's Game of Life

 

We can store the actual cells themselves using a dictionary. Each cell in the
grid can have two possible states; alive or dead. There are various ways we
could initialize the grid. We could initialize the grid with random values
using **random.choice** from the random module, for instance:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cells = {(c, r): random.choice([True, False]) for c in range(columns) for r in range(rows)}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can use **random.choice** to choose between any values in a list or sequence.
The above code would initialize our grid with a similar amount of live and dead
cells, but it’d be better if we could control the starting population, because
different population densities have a different evolution.

 

Another possibility would be to pass in the starting population:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_cells(population=100):
    cells = {(c, r): False for c in range(columns) for r in range(rows)}
    for i in range(population):
        col = random.randint(0, columns)
        row = random.randint(0, rows)
        cells[col, row] = True
    return cells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

**Line 1:** We allow the desire population to be passed in, or default to 100.

 

**Line 2:** We set every cell in the grid to be dead.

 

**Lines 3-6: **We add a certain amount of live cells, by setting the dictionary
entry to **True**.

 

This version has several problems though. For a start, it has a bug in that we
could set the same cell to True several times, so it’s quite likely the
population will be less than we specified. It also has the problem that every
time you want to change the grid size, you’ll have to change the population.

 

It would be better if we could specify a population density:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_cells(density=0.2):
    return {(c, r): random.random() < density for c in range(columns) for r in 
range(rows)}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

**Random.random()** returns a number between 0 and 1. If this number is less
than 0.2, **random.random() density**evaluates to True. This line might seem
quite confusing, but it’s just a slightly more condensed version of this:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_cells(density=0.2):
    cells = {}
    for c in range(columns):
        for r in range(rows):
            if random.random() < density:
                cells[c, r] = True
            else:
                cells[c, r] = False
    return cells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We can draw the cells with the
following [function](http://codeinstitute.wpengine.com/glossary/function/):

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def draw_cells():
    for (x, y) in cells:
        colour = green if cells[x, y] else black
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, colour, rectangle)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

**Line 3:** We assign a colour based on the
cell [state](http://codeinstitute.wpengine.com/glossary/state/).

 

**Line 4:** We define a rectangle using the coordinates of the top left corner,
and the size of the rectangle.

 

**Line 5:** We can draw a rectangle by passing in the screen, colour, and
rectangle coordinates.

 

The full program should now look like this:

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
 
 
def get_cells(density=0.2):
    return {(c, r): random.random() < density for c in range(columns) for r in range(rows)}
 
 
def draw_cells():
    for (x, y) in cells:
        colour = green if cells[x, y] else black
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, colour, rectangle)
 
 
pygame.init()
columns, rows = 50, 50
cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)
cells = get_cells()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
    draw_cells()
    draw_grid()
 
    pygame.display.update()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

Notice that in **line 39** we’re drawing the cells before the grid, otherwise
the cells would overwrite the grid. The output should now look something like
this:

![](img/1.png)

 

Try changing the value of density and see what happens.
