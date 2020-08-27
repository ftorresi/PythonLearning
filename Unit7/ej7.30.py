from math import sqrt
class Vec3D:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
        
        def __add__(self, other):
            if isinstance(other, (list,tuple)):
                other = Vec3D(other[0],other[1],other[2])
            elif not (hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z')):
                raise TypeError('other must have x, y and z attr.')
            return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)
        
        def __radd__(self, other):
            return self.__add__(other)
        
        def __sub__(self, other):
            if isinstance(other, (list,tuple)):
                other = Vec3D(other[0],other[1],other[2])
            elif not (hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z')):
                raise TypeError('other must have x, y and z attr.')
            return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)
        
        def __rsub__(self, other):
            if isinstance(other, (list,tuple)):  #make other a Vec3D object in order to use other.__sub__
                other = Vec3D(other[0],other[1], other[2])  #since __sub__ is not defined for list/tuple
            elif not (hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z')):
                raise TypeError('other must have x, y and z attr.')              
            return other.__sub__(self)
        
        def __mul__(self, other):              
            return self.x*other.x + self.y*other.y + self.z*other.z
        
        def __abs__(self):
            return sqrt(self.x**2 + self.y**2 + self.z**2)
        
        def __eq__(self, other):
            return self.x == other.x and self.y == other.y and self.z == other.z
        
        def __str__(self):
            return '(%g, %g, %g)' % (self.x, self.y, self.z)
        
        def __ne__(self, other):
            return not self.__eq__(other) # reuse __eq__
        
        def cross(self, other):
            sx, sy, sz = self.x, self.y, self.z
            ox, oy, oz=other.x, other.y, other.z
            xc=sy*oz-sz*oy
            yc=sz*ox-sx*oz
            zc=sx*oy-sy*ox            
            return Vec3D(xc, yc, zc)
        


u = Vec3D(0,1, 2)
v = Vec3D(2, 1,0)
w = Vec3D(2,2,2)
a = u + v
print (a)
print(w==a)
print(w!=a)
a = u + (1,2, 3)
print (a)
a = [1,2,3]+u
print (a)
a = u - (1,2,3)
print (a)
a = [1,2,3]-u
print (a)
a=Vec3D(2,2,1)
print(abs(a))
print(v*u)
print(u*w)
u = Vec3D(0,1, 0)
v = Vec3D(0,0,1)
a= u.cross(v)
print(a)
a= a.cross(u)
print(a)
a= a.cross(v)
print(a)









