import math

def feq(x,y):
    "float equality because python sucks"
    return abs(x-y) <= .0000001


class Point(object):
    """2D point utility class"""
    
    x = 0.0
    
    y = 0.0
    
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (feq(self.x, other.x) and feq(self.y,other.y))

    def __add__(self, p2):
        """add points"""
        return Point(self.x + p2.x, self.y + p2.y)


    def __sub__(self, p2):
        """subtract points"""
        p2.negate()
        return self + p2

    
    def __mul__(self, scalar):
        if isinstance(scalar,(int, long, float, complex)):
            return Point(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("unsupported operand type(s) for *: '{}' and '{}'").format(self.__class__, type(other))

        
    def negate(self):
        """self * -1"""
        self = self * -1.0

    def __str__(self):
        """(x,y)"""
        return '(%f,%f)' % (self.x,  self.y)


class Vector(Point):
    """2D Vector utility class derived from point"""
    
    def magnitude(self):
        return math.sqrt(self.x**2.0 + self.y**2.0)


    def isNormal(self):
        return (feq(self.magnitude(), 1.0))

        
    def normalize(self):
        scalar = 1/self.magnitude()
        self.x = self.x * scalar
        self.y = self.y * scalar


    def __mul__(self, other):
        if isinstance(other, (Point)):
            return other.x*self.x + other.y*self.y
        else:
            return super(Vector, self).__mul__(other)

        
    def cross(self, other):
        print "NOT IMPLEMENTED"

class Rect(object):
    "Rectangle class"
    
    def __init_(self,  width=1, height=1):
        self.width = 0.0
        self.height = 0.0

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return self.width*2 + self.height*2
        


    
