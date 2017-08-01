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

# define our method to draw the cells on our grid
def draw_cells():
    for(x, y) in cells:
        colour = green if cells[x, y] else black
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, colour, rectangle)

        # define our method to get the neighbours of our grid cell
def get_neighbours((x, y)):
    positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                 (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
    return [cells[r, c] for (r, c) in positions if 0 <= r < rows and 0 <= c < columns]

# define our method to evolve the cells depending on the number of neighbours and alive state
def evolve():
    for position, alive in cells.items():
        live_neighbours = sum(get_neighbours(position))
        if alive:
            if live_neighbours < 2 or live_neighbours > 3:
                cells[position] = False
        elif live_neighbours == 3:
            cells[position] = True

# create a method that returns a dictionary to store & initialise our cells
# NOTE: each cell can have 2 possible states:
# Alive OR Dead
def get_cells(density = 0.2):
    return {(c, r): random.random() < density for c in range(columns) for r in range(rows)}

# call the initialise method
pygame.init()

# define our grid properties
columns, rows = 50, 50
cells = get_cells()

cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

# call on our loop to repeat until the exit condition is True
while True:
    clock.tick(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # call our draw cells & draw grid methods every frame
    draw_cells()
    evolve()
    draw_grid()

    # update/refresh the game window
    pygame.display.update()
