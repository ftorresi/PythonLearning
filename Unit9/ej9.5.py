class Ellipse:
    def __init__(self,x0, y0, a, b):
        self.x0, self.y0, self.a, self.b = x0, y0, a, b
        
    def area(self):
        return pi*self.a*self.b
        
class Circle(Ellipse):
    def __init__(self, x0, y0, R):
        Ellipse.__init__(self, x0, y0, R, R)
       
    def circumference(self):
            return 2*pi*self.a
        
from math import pi
e=Ellipse(0,0,5,3)
print(e.area())
c=Circle(0,0,5)
print(c.area())
print(c.circumference())
