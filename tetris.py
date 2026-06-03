import pygame
import random
from tetris_logic import Tetris

# Initialize Pygame
pygame.init()
# Set up display
f= Tetris()

BLOCK_SIZE = 30
WIDTH, HEIGHT = f.height * BLOCK_SIZE, f.width * BLOCK_SIZE
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

board = f.grid

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                
                    print("Moved selection up")
                elif event.key == pygame.K_DOWN:
                    
                    print("Moved selection down")
                elif event.key == pygame.K_LEFT:
                    print("Left arrow pressed")
                elif event.key == pygame.K_RIGHT:
                    print("Right arrow pressed")

         

    # RENDER YOUR GAME HERE
    for r in range(board.shape[0]):
        for c in range(board.shape[1]):
            color = COLORS[board[r][c]]
            pygame.draw.rect(screen, color, (c*30, r*30, 30, 30))
            pygame.draw.rect(screen, BLACK, (c*30, r*30, 30, 30), 1)  # draw grid lines
    
    frame_count+= 1
    if frame_count%20 == 0:
        board = f.step()  

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()