from math import sqrt
class Vec2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __add__(self, other):
            if isinstance(other, (list,tuple)):
                other = Vec2D(other[0],other[1])
            elif not (hasattr(other, 'x') and hasattr(other, 'y')):
                raise TypeError('other must have x and y attr.')
            return Vec2D(self.x + other.x, self.y + other.y)
        
        def __radd__(self, other):
            return self.__add__(other)
        
        def __sub__(self, other):
            if isinstance(other, (list,tuple)):
                other = Vec2D(other[0],other[1])
            elif not (hasattr(other, 'x') and hasattr(other, 'y')):
                raise TypeError('other must have x and y attr.')
            return Vec2D(self.x - other.x, self.y - other.y)
        
        def __rsub__(self, other):
            if isinstance(other, (list,tuple)):  #make other a Vec2D object in order to use other.__sub__
                other = Vec2D(other[0],other[1])  #since __sub__ is not defined for list/tuple
            elif not (hasattr(other, 'x') and hasattr(other, 'y')):
                raise TypeError('other must have x and y attr.')                
            return other.__sub__(self)
        
        def __mul__(self, other):              
            return self.x*other.x + self.y*other.y
        
        def __abs__(self):
            return sqrt(self.x**2 + self.y**2)
        
        def __eq__(self, other):
            return self.x == other.x and self.y == other.y
        
        def __str__(self):
            return '(%g, %g)' % (self.x, self.y)
        
        def __ne__(self, other):
            return not self.__eq__(other) # reuse __eq__


u = Vec2D(0,1)
v = Vec2D(1,0)
w = Vec2D(1,1)
a = u + v
print (a)
a = u + (1,2)
print (a)
a = [1,2]+u
print (a)
a = u - (1,2)
print (a)
a = [1,2]-u
print (a)









