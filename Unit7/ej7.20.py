from math import sin, pi
import numpy as np

class Heaviside:
    
    def __init__(self,eps=None):
            self.eps=eps
        
    def __call__(self,x):
        eps=self.eps
        r=np.zeros_like(x)
        if eps==None:
            condition=x>=0
            r[condition]=1.0
            
        else:
            x=np.asarray(x)
            condition1=np.logical_and(-eps<=x , x<=eps)
            condition2=x>eps
            
            r[condition1]=0.5+x[condition1]/(2*eps)+np.sin(np.pi*x[condition1]/eps)/(2*np.pi)
            r[condition2]=1.0
        
        return r



class Indicator:
    def __init__(self, a, b, eps=None):
        self.a, self.b, self.eps=a, b, eps
        
    def __call__(self,x):
        a, b, epsilon=self.a, self.b, self.eps
        if epsilon==None:
            H=Heaviside()
        else:
            H=Heaviside(epsilon)
        return H(x-a)*H(b-x)
    
#a,b=0,2  
#I = Indicator(a, b)
## indicator function on [a,b]
#print (I(a-1.0), I(b+0.1), I((a+b)/2.0))
#x=np.linspace(-0.5,2.5,16)
#print(I(x))
#I = Indicator(a, b, eps=1.0)
## smoothed indicator function on [0,2]
#print (I(0), I(1), I(1.9))
#print(I(x))
