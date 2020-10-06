class SuperDer:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)
        
    def __call__(self, x):
        raise NotImplementedError('___call__ missing in class %s' % self.__class__.__name__)
    

class Derivative(SuperDer):
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x+h)-f(x))/h
    
class Backward(SuperDer):
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x)-f(x-h))/h
    
class Central(SuperDer):
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x+h)-f(x-h))/(2*h)
   
from math import exp, sin  

c=Central(Central(sin,0.5E-5),0.5E-5)
x=1
print sin(x),c(x)
print "Seems to work OK to calculate 2nd derivatives, maybe with more error than using the formula for 2nd derivative straightforwardly"
