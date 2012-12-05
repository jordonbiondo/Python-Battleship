from Geometry2D import *

from Enums import *

class Ship(object):
    """A battleship, has a position, and extends 'length' spaces in its direction"""
    
    def __init__(self, position=Point(), direction=Direction.Up, length=2, name="ship"):
        self.position = position
        self.direction = direction
        self.length = length
        self.hits = 0
        self.name = name


    def youSunkMyBattleShip(self):
        return self.hits == self.length


    def takeHit(self):
        self.hits = self.hits + 1

        
    def coverage(self):
        """Returns a list or points covered by the ship"""
        return [self.position + self.direction*i for i in range(self.length) ]

    
    def covers(self, point):
        return point in self.coverage()

