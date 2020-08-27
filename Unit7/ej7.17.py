from math import *

class Backward:
    def __init__(self, f, h=1e-9): #Having imported math, e is now the Euler constant, so we have to write 1e-9
        self.f, self.h = f, h
        
    def __call__(self, x):
        h, f = self.h, self.f
        return (f(x) - f(x-h))/h # finite difference
        
dsin = Backward(sin)  #In this case, using h=1e-9 works perfectly.
e = dsin(0) - cos(0); print ('error:', e)
dexp = Backward(exp, h=1e-7) #Having imported math, e is now the Euler constant, so we have to write 1e-7
e = dexp(0) - exp(0); print ('error:', e)
