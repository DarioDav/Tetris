import numpy as np

import random

#Tetris_pieces class
# It takes an array representing the board and a list containing the shapes of the pieces    
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
        
        self.current_position = [0,5]

    def select_piece (self):
        key = random.choice(list (self.pieces.keys()))
        piece = self.pieces["SQ"]
        
    
        top, left = self.current_position[0], self.current_position[1]
        #Spawn a line
        ph, pw = piece.shape
        
        for r in range (ph):
            for c in range (pw):
                if piece[r,c]!= 0:
                    self.grid[top + r, left + c] = 1


        print(self.grid)

    # def rotate_piece(self):
    #     np.rot90(self.pieces[n])
        
    def move_piece_down (self):
        # coords = np.argwhere(self.grid == 1)
        # print (coords)
        
        # for n in coords:
            
        #     # self.grid[n[0]][n[1]]= 0
        #     self.grid[n[0] +1][n[1]]= 1

        self.current_position[0] =+ 1
        print(self.current_position)
        self.spawn_piece()
            
        print("NEW GRID")
        print(self.grid)
    
    def rotate_piece(self):

        np.rot90(self)


if __name__ == "__main__":
    tetris = Tetris()

    tetris.spawn_piece()
    tetris.move_piece_down()
