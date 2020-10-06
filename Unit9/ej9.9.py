class FuncWithDerivatives:
    def __init__(self, h=1.0E-5):
        self.h = h # spacing for numerical derivatives
    
    def __call__(self, x):
        raise NotImplementedError('___call__ missing in class %s' % self.__class__.__name__)
    
    def df(self, x):
        """Return the 1st derivative of self.f."""
        # Compute first derivative by a finite difference
        h = self.h
        return (self(x+h) - self(x-h))/(2.0*h)
    
    def ddf(self, x):
        """Return the 2nd derivative of self.f."""
        # Compute second derivative by a finite difference:
        h = self.h
        return (self(x+h) - 2*self(x) + self(x-h))/(float(h)**2)


class Sin1(FuncWithDerivatives):
    def __call__(self, x):   
        return sin(x)
    
class Sin2:
    def __call__(self, x):
        return sin(x)
    
    def df(self, x):
        return cos(x)
    
    def ddf(self, x):
        return -sin(x)
    

from math import sin, cos,pi
s1=Sin1()
s=Sin2()
xv=[0,pi/4,pi/2]
for x in xv:
    print("x=%g, sin(x)=%g" %(x, s(x)))
    print("exact derivative=%g, approx. derivative=%g" %(s.df(x), s1.df(x)))
    print("exact 2nd derivative=%g, approx. 2nd derivative=%g" %(s.ddf(x), s1.ddf(x)))
