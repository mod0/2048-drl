import numpy as np
import numpr.random as nr

class TwoZeroFourEight():

    # Store all empty tuples where next tile can be
    # placed
    empty_cells = dict()

    # Starter tiles
    starter_tiles = [2, 4]
    
    def __init__(self, n):
        self.n    = n
        self.game = np.zeros((n,n), dtype=np.int32)
        for i in xrange(n):
            for j in xrange(n):
                empty_cells[(i, j)] = 0
        location, value = generate_random_tile()
        game[location] = value
        empty_cells.pop(location, None)
        location, value = generate_random_tile()
        game[location] = value
        empty_cells.pop(location, None)
        

    def generate_random_tile():
        # Choose an empty_cell randomly
        # Generate a number from starter_tile list
        keys          = empty_cells.keys()
        # Check for game over?
        index         = nr.randint(len(keys))
        location      = keys[index]
        starter_index = nr.randint(len(starter_tiles))
        value         = starter_tiles[starter_index]
        return location, value

    
    def slide_right(self, dryrun = False):
        # Start at the penultimate column from right and
        # check what can be combined.
        moves_possible = False
        
        for c in reversed(xrange(0, self.n - 1)):
            for r in xrange(0, n):
                # If the current cell is not empty
                if self.game[r, c] > 0:
                    # Can we combine with the one to the right?
                    if self.game[r, c] == self.game[r, c + 1]:
                        # Yes we can
                        moves_possible = True
                        # Then combine and introduce an empty cell here.
                        if not dryrun:
                            self.merge_right(r, c)
                            # Now move the combined cell as far right
                            self.move_tile_right(r, c + 1)
                        else:
                            return moves_possible
                    else:
                        # Move the current cell as far right as possible
                        moves_possible = (moves_possible or self.move_tile_right(r, c, dryrun))
                        if dryrun:
                            return moves_possible

        return moves_possible

                        
    def merge_right(self, r, c):
        self.game[r, c + 1] *= 2
        self.game[r, c]      = 0
        # Push the key into empty_cells dictionary
        empty_cells[(r,c)]   = 0

        
    def move_tile_right(self, r, c, dryrun = False):
        moves_possible = False

        # Find location of last empty cell in this direction
        last_empty_cell = None
        for cc in xrange(c + 1, self.n):
            # Check if this is an empty cell
            # and keep track of last empty cell 
            if self.game[r, cc] == 0:
                last_empty_cell = (r, cc)
                
        # Now move the cell to that location
        if last_empty_cell is not None:
            if not dryrun:
                self.game[last_empty_cell] = self.game[r, c]
                empty_cells.pop(last_empty_cell, None)
                self.game[r, c]     = 0
                # Push the key into empty_cells dict
                empty_cells[(r, c)] = 0
            else:
                moves_possible = True

        return moves_possible
