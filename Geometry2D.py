import math

def feq(x,y):
    """float equality because python sucks"""
    return abs(x-y) <= .0000001


class Point(object):
    """2D point utility class"""

    def __init__(self, x=0.0, y=0.0):
        """Init from x, y"""
        self.x = x
        self.y = y


    def __eq__(self, other):
        """equality: coords are equal"""
        return (feq(self.x, other.x) and feq(self.y,other.y))
    

    def __add__(self, p2):
        """add points"""
        return Point(self.x + p2.x, self.y + p2.y)


    def __sub__(self, p2):
        """subtract points"""
        return self + p2.negated()

    
    def magnitude(self):
        return math.sqrt(self.x**2.0 + self.y**2.0)


    def isNormal(self):
        return (feq(self.magnitude(), 1.0))

            
    def normalized(self):
        scalar = 1/self.magnitude()
        return Point(self.x * scalar, self.y * scalar)

    
    def normalize(self):
        self = self.normalized()


    def dot(self, other):
        return other.x*self.x + other.y*self.y


    def scale(self, scalar):
        self = self.scaled(scalar)


    def scaled(self, scalar):
        return Point(self.x * scalar, self.y * scalar)


    def __mul__(self, other):
        if isinstance(other, (Point)):
            return self.dot(other)
        else:
            self.scale(other)

    
    def __div__(self, scalar):
        return self * (1.0/scalar)

        
    def negate(self):
        """self * -1"""
        self = self * -1.0


    def negated(self):
        return Point(self.x*-1.0, self.y * -1.0)


    def __str__(self):
        """(x,y)"""
        return '(%f,%f)' % (self.x,  self.y)

""" Vector Alias """
Vector = Point
