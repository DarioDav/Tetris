import numpy as np

import random

#Tetris_pieces class
  
class Tetris:
    def __init__(self, width = 20, height = 10 ):
        self.width= width
        self.height = height

        #Create an array of zeros to represent the board
        self.grid = np.zeros((width,height))

        #dictionary with all the pieces
        self.pieces = {
            "L" :  np.array([  [1,0],
                        [1,0],
                        [1,1]]),

            "SQ" : np.array( [[1,1],
                            [1,1]]),

            "Z" :  np.array( [[1,1,0],
                            [0,1,1]]),

            "V" :  np.array( [ [1],
                            [1],
                            [1],
                            [1]])}
        

        self.current_position = np.array([0,5])
        self.current_piece = None

    def spawn_piece (self):
        key = random.choice(list (self.pieces.keys()))# picks one of the pieces at random
        piece = self.pieces["SQ"] #kept no square for now, change for key later
        return piece

    def draw_piece (self, piece):
        #draws the piece in the board at the current position
        
        top, left = self.current_position[0], self.current_position[1]
    
        ph, pw = piece.shape
        grid = self.grid.copy()
        
        for r in range (ph):
            for c in range (pw):
                if piece[r,c]!= 0:
                    grid[top + r, left + c] = piece[r,c]
        return grid

        
    def move_piece_down (self):

        new_top = self.current_position[0] + 1
        new_left = self.current_position[1] + 0

        print(new_top)
        self.current_position = [new_top, new_left]
        return True
        
            
    
    def rotate_piece(self):

        np.rot90(self)

    def step(self):
        piece = self.spawn_piece()
        
        board = self.draw_piece(piece)
        print(board)
        self.move_piece_down()
        return board
        

if __name__ == "__main__":
    tetris = Tetris()
    for s in range(5):
        tetris.step()