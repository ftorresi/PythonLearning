class F:
    def __init__(self, a, b):
        self.a, self.b = a, b
    
    def __call__(self, t):
        return exp(-self.a*t)*sin(self.b*t)


class Fb(F):
    def __init__(self, a, t):
        self.a, self.t = a, t
    
    def __call__(self, b):
        F.__init__(self,self.a,b)
        value=F.__call__(self,self.t)
        return value
     
from math import sin, exp
f = Fb(t=1.57079633, a=0.5)
print (f(0),f(1),f(2)) 
