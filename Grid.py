class Grid(object):
    
    def __init__(self, size):
        self.size = 10
        self.grid = [[None] * size] * size
    
    def place(self, x, y, thing):
        self.grid[x][y] = thing
    
    def get(self, x,y):
        return self.grid[x][y]

    def columns(self):
        return self.grid
    
