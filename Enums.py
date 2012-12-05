from Geometry2D import *

class Direction(object):
    """Until a better enumeration method is found"""
    Right = Vector(1, 0)
    Left = Vector(-1, 0)
    Up = Vector (0, 1)
    Down = Vector(0, -1)

class Status(object):
    Inactive = ' '
    Miss = '*'
    Hit = 'x'
    Sunk = 'X'
    
