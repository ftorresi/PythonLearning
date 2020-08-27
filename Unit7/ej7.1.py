from math import exp, sin

class F:
    
    def __init__(self,a,w):
        self.a, self.w= a, w
    
    def value(self,x):
        return exp(-self.a*x)*sin(self.w*x)
