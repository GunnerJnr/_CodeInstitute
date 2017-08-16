# import the system and pygame files needed
import sys
import pygame

# import our newly created colours file
from colours import green

# define our grid method
def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, green, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, green, (0, y), (width, y))

# call the initialise method
pygame.init()

# define our grid properties
columns, rows = 50, 50
cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)

# call on our loop to repeat until the exit condition is True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # call our draw grid method every frame
    draw_grid()

    # update/refresh the game window
    pygame.display.update()
