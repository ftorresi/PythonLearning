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
    
class Parabola0(Line):
    pass

l=Line(1,2)
p=Parabola0(1,2)

print(dir(l))
print(dir(p))
print(dir(p)==dir(l)) #Same thing
print(l.__dict__)
print(p.__dict__)
