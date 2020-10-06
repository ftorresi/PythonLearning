class Line:
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
        
    def __call__(self, x):
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
        return Line.__call__(self, x) + self.c2*x**2


class Sinquad(Parabola):
    def __init__(self, A, w, a, b, c):
        Parabola.__init__(self, c, b, a) # let Parabola deal with the cuadratic part
        self.A, self.w = A, w
    
    def __call__(self, x):
        return Parabola.__call__(self, x) + self.A*sin(self.w*x)
    
    
from math import pi, sin    
f=Sinquad(2,0.5,1,1,1)
print(f(5))
print(f.table(0,3,13))

    
