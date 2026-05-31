import numpy as np

import random


grid = np.array( [
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [2., 2., 2., 2., 2., 2., 2., 2., 2., 2.]])



L = L = np.array([  [1,0],
                    [1,0],
                    [1,1]])

SQ = np.array( [[1,1],
                [1,1]])

Z =  np.array( [[1,1,0],
                [0,1,1]])

V =  np.array( [ [1],
                 [1],
                 [1],
                 [1]])

pieces = [L, SQ, Z, V]

    



#Tetris_pieces class
# It takes an array representing the board and a list containing the shapes of the pieces    
class Tetris_piece:
    def __init__(self, grid, pieces):

        self.grid = grid
        self.pieces = pieces

    def spawn_piece (self):
        random.choice(self.pieces)
        spawn = [0, np.random.randint(0, self.grid.shape[1])]
        self.grid [spawn[0],spawn[1]]=1
        print(self.grid)

    # def rotate_piece(self):
    #     np.rot90(self.pieces[n])
        
    def move_piece_down (self):
        coords = np.argwhere(grid == 1)
        print (coords)
        print("NEW GRID")
        print(grid)
        for n in coords:
            grid[n[0]][n[1]]= 0
            grid[n[0] +1][n[1]]= 1

        print(grid)
    
    def rotate_piece(self):
        np.rot90(self)



tetris = Tetris_piece(grid=grid, pieces=pieces)

tetris.spawn_piece()
tetris.move_piece_down()

        
        

        
        

