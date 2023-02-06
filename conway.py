import pygame
import numpy as np
import time

# initialize pygame
pygame.init()

# set window size and title
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Conway\'s Game of Life')

# initialize grid with random states
grid_size = (80, 60)
grid = np.random.choice([0, 1], grid_size)

# set cell size based on window size and grid size
cell_size = width // grid_size[0]

# define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

# function to update grid
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            neighbors = (grid[i-1, j-1] + grid[i-1, j] + grid[i-1, (j+1)%grid_size[1]] + 
                        grid[i, j-1] + grid[i, (j+1)%grid_size[1]] + 
                        grid[(i+1)%grid_size[0], j-1] + grid[(i+1)%grid_size[0], j] + grid[(i+1)%grid_size[0], (j+1)%grid_size[1]])
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if neighbors == 3:
                    new_grid[i, j] = 1
    return new_grid

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill window with black color
    window.fill(black)
    
    # update grid
    grid = update_grid(grid)
    
    # draw grid
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if grid[i, j] == 1:
                pygame.draw.rect(window, white, (i*cell_size, j*cell_size, cell_size, cell_size))
    
    # update display
    pygame.display.update()
    
    # add delay
    time.sleep(0.1)

# quit pygame
pygame.quit()
