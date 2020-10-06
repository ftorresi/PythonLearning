class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
        
    def __call__(self, x):
        print("call Line")
        return self.c0 + self.c1*x
    
    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s =''
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s
    
    
class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1) # let Line store c0 and c1
        self.c2 = c2
    
    def __call__(self, x):
        print("call Parabola")
        return Line.__call__(self, x) + self.c2*x**2


class Cubic(Parabola):
    def __init__(self, c0, c1, c2,c3):
        Parabola.__init__(self, c0, c1,c2) # let Parabola store c0, c1 and c2
        self.c3 = c3
    
    def __call__(self, x):
        print("call Cubic")
        return Parabola.__call__(self, x) + self.c3*x**3
    
    
class Poly4(Cubic):
    def __init__(self, c0, c1, c2,c3,c4):
        Cubic.__init__(self, c0, c1,c2,c3) # let Parabola store c0, c1, c2 and c3
        self.c4 = c4
    
    def __call__(self, x):
        print("call Poly4")
        return Cubic.__call__(self, x) + self.c4*x**4
    
c=Cubic(1,1,1,1)
print(c(1))
p=Poly4(1,1,1,1,1)
print(p(1))
    
