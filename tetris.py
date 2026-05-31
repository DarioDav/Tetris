import pygame
import random
import tetris_logic
from tetris_logic import Tetris_piece

# Initialize Pygame
pygame.init()
# Set up display
GRID = tetris_logic.grid
PIECES = tetris_logic.pieces
f= Tetris_piece(GRID, PIECES)

BLOCK_SIZE = 30
WIDTH, HEIGHT = GRID.shape[1] * BLOCK_SIZE, GRID.shape[0] * BLOCK_SIZE
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
    for r in range(GRID.shape[0]):
        for c in range(GRID.shape[1]):
            color = COLORS[GRID[r][c]]
            pygame.draw.rect(screen, color, (c*30, r*30, 30, 30))
            pygame.draw.rect(screen, BLACK, (c*30, r*30, 30, 30), 1)  # draw grid lines
    

    frame_count+= 1
    if frame_count%10 == 0:
        f.spawn_piece()
        f.move_piece_down()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()