import pygame
import random
import tetris_logic
from tetris_logic import Tetris

# Initialize Pygame
pygame.init()
# Set up display
f= Tetris()

BLOCK_SIZE = 30
WIDTH, HEIGHT = f.grid.shape[1] * BLOCK_SIZE, f.grid.shape[0] * BLOCK_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

COLORS = {0: (125,125,125), 
          1: (255, 0, 0), 
          2: (0, 255, 0)}



#set up the game clock
clock = pygame.time.Clock()
running = True
frame_count= 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            

    # RENDER YOUR GAME HERE
    for r in range(f.grid.shape[0]):
        for c in range(f.grid.shape[1]):
            color = COLORS[f.grid[r][c]]
            pygame.draw.rect(screen, color, (c*30, r*30, 30, 30))
            pygame.draw.rect(screen, BLACK, (c*30, r*30, 30, 30), 1)  # draw grid lines
    

    frame_count+= 1
    if frame_count%10 == 0:
        f.spawn_piece()
        

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()