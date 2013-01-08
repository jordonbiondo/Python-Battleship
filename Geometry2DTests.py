from Geometry2D import *
import math

a = Point(3, 3)
b = Point(4, 4)

assert (a + Point(1, 1) == b) # adding

assert(Point(3, 3).magnitude() == math.sqrt(18)) # magnitude

assert(Point(3, -5) + Point(-10, -10) == Point(3, -5) - Point(10, 10)) # add sub

assert(not Point(3, 3).isNormal()) # normal

assert(Point(0, 1).isNormal()) #normal 

assert(Point(349, 8943).normalized().isNormal()) # normal

assert(Point(3, 4) * Point(2, -2) == -2) #dot

assert(Point(3.00000, 4.00000) == Point(3, 4)) # numbeic types
