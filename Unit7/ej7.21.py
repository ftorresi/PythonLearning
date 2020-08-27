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

class PiecewiseConstant:
    
    def __init__(self,data,xmax): #data=[(xi,vi)]
        self.data, self.xmax=data, xmax
        
    def __call__(self,x):
        x=np.asarray(x)
        val=np.zeros_like(x,dtype=float)
        data,xmax=self.data,self.xmax
        for i in range(len(data)-1):
            I=Indicator(data[i][0],data[i+1][0])
            val+=data[i][1]*I(x)
            #print val
        I=Indicator(data[-1][0],xmax)
        val+=data[-1][1]*I(x)
        
        for i in range(len(data)): #correct values for f(x) in each interval extreme
            condition=x==data[i][0]
            val[condition]=data[i][1]
               
        return val
    
    def plot(self):
        data,xmax=self.data,self.xmax
        x0=[]
        for i in range(len(data)-1):           #build the x to be plotted this way, so as to use the least number of points and plot the steps with vertical lines instead of (possibly) diagonals
            x=[data[i][0],data[i+1][0]-0.001]
            x0.extend(x)
        x0.extend([data[-1][0],xmax])
        x0=np.asarray(x0)
        y0=self.__call__(x0)
        return x0, y0


#f = PiecewiseConstant([(1,0.4), (1.5,0.2), (3, 0.1)], xmax=4)
#print (f(1), f(1.5), f(1.75),f(3), f(4))  
#x=np.linspace(0.5,4.5,41)
#print(f(x))
    
#x, y = f.plot()
#from matplotlib.pyplot import plot, show
#plot(x, y)    
#show()
    
