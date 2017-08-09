Creating and Drawing A Grid
===========================

 

To draw a grid, we can use `pygame.draw.line` to draw horizontal and vertical
lines. We’ll have to give the grid lines a colour, so let’s define some colours
first in a separate file called `colours.py`:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
dark_blue = 0, 0, 128
white = 255, 255, 255
black = 0, 0, 0
pink = 255, 200, 200
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

We define colours by specifying their red, green and blue (`RGB`) components. We
use range (`start`, `stop`, `step`) in our `draw_grid` function to draw our
lines, where `stop=width` and `step=cell_size`.

The `draw.line` function takes the arguments:

-   `screen:` our screen we defined earlier

-   `colour:` we can import this from our `colours.py` file

-   `line start:` the start of the line given as `x,y` coordinates

-   `line end:` the end of the line given as `x,y` coordinates

 

Here’s the program so far:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sys
 
import pygame
 
from colours import dark_blue
 
 
def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, dark_blue, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, dark_blue, (0, y), (width, y))
 
 
pygame.init()
 
columns, rows = 100, 50
cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
    draw_grid()
 
    pygame.display.update()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

`Line 5:` Notice our imports are now in the recommended order: built-in modules,
then 3rd party modules, then modules within our project.

 

`Line 27:` We call `draw_grid` every frame.

 

`Line 29:` We have to call `display.update()`to actually see our changes.

 

You should now see a grid like this:

![](img/1.png)
