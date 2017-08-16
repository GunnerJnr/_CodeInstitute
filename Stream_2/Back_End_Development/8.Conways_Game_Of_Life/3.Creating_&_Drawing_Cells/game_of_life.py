# import the system and pygame files needed
import random
import sys
import pygame

# import our newly created colours file
from colours import dark_blue, green, black

# define our grid method
def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, dark_blue, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, dark_blue, (0, y), (width, y))

# create a method that returns a dictionary to store & initialise our cells
# NOTE: each cell can have 2 possible states:
# Alive OR Dead
def get_cells(density = 0.2):
    return {(c, r): random.random() < density for c in range(columns) for r in range(rows)}

# define our method to draw the cells on our grid
def draw_cells():
    for(x, y) in cells:
        colour = green if cells[x, y] else black
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, colour, rectangle)

# call the initialise method
pygame.init()

# define our grid properties
columns, rows = 50, 50
cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)
cells = get_cells()

# call on our loop to repeat until the exit condition is True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # call our draw cells & draw grid methods every frame
    draw_cells()
    draw_grid()

    # update/refresh the game window
    pygame.display.update()
