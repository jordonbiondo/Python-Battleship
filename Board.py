from Enums import *
from Geometry2D import *
from Ship import *

class Board(object):

    def __init__(self, size):
        self.grid = [[Status.Inactive for n in range(size)] for i in range(size)]
        self.ships = []

    def size(self):
        return len(self.grid)
    
    def statusAt(self, coords):
        return self.grid[coords.x][coords.y]

    
    def isInactive(self, coords):
        return self.statusAt(coords) == Status.Inactive


    def receiveFire(self, coords):
        if self.isInactive(coords):
            self.takeFire(coords)
            return True
        else:
            return False
        
    def takeFire(self, coords):
        for s in self.ships:
            if coords in s.coverage():
                self.markHit(coords)
                s.takeHit()
                didSink = tryToSink(s)
                # Fill me in with stuff
                return True
        self.markMiss(coords)    
        return False


    def mark(self, coords, status):
        """mark a grid position with a status"""
        self.grid[coords.x][coords.y] = status


    def markHit(self, coords):
        self.mark(coords, Status.Hit)

        
    def markMiss(self, coords):
        self.mark(coords, Status.Miss)

    def tryToSink(self, ship):
        if ship.youSunkMyBattleShip:
            for p in ship.coverage():
                self.mark(p, Status.Sunk)
            return True
        else:
            return False
        
    def __str__(self):
        value = "\t "
        for c in range(self.size()):
            value = value + " "+str(c+1)
        value = value+ "\n"
        for r in range(self.size()):
            value = value + "\t|"
            for c in range(self.size()):
                if c <> self.size():
                    value = value+ " "
                value = value + self.grid[c][r]
            value = value + " | " + str(r+1)+ "\n"
        return value
        
        
   
