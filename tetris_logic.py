import numpy as np

import random

  
class Tetris:
    def __init__(self, height = 20, width = 10 ):
        self.height= height
        self.width = width

        #Create an array of zeros to represent the board
        self.grid = np.zeros((height,width))

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
        self.current_piece = self.pieces[key].copy() #kept no square for now, change for key later
        

    def draw_piece (self ):
        #draws the piece in the board at the current position
        
        top, left = self.current_position[0], self.current_position[1]
    
        ph, pw = self.current_piece.shape
        grid = self.grid.copy()
        
        for r in range (ph):
            for c in range (pw):
                if self.current_piece[r,c]!= 0:
                    grid[top + r, left + c] = self.current_piece[r,c]
        return grid

        
    def move_piece_down (self, dx = 0, dy= 1 ):

        new_top = self.current_position[0] + dy
        new_left = self.current_position[1] + dx

        print(new_top)
        self.current_position = [new_top, new_left]
        if self.check_position()==False:
            return False
        return True
        
            
    def check_position (self):
        if self.current_piece is None:
            return False
        elif self.current_position[0] + self.current_piece.shape[0] > self.height:
            return False
        elif self.current_position[1] + self.current_piece.shape[1] > self.width or self.current_position[1] < 0:
            return False
        return True

    
    def rotate_piece(self):
        if self.check_position()== True:
            self.current_piece = np.rot90(self.current_piece)
        else:
            self.current_piece = None

    def step(self):
        if self.current_piece is None:
            self.spawn_piece()
        
        board = self.draw_piece()
        print(board)
        self.move_piece_down()
        if self.check_position()==False:
            self.current_piece = None
            self.current_position = np.array([0,5])
        self.rotate_piece()

        return board
        

if __name__ == "__main__":
    tetris = Tetris()
    
    tetris.step()
    print(tetris.height)
    