from math import floor #to use in test
import numpy as np
import matplotlib.pyplot as plt

dat=[(0,-1),(1,0),(1.5,4),(2,3)] 

def piecewise(x, data): #data=[(xi,vi)]
    if x<data[0][0]:
        print ( "argument must be greater than %.2f" %data[0][0])
        return None
    for i in range(len(data)): #first check if x=xi for any i
        if x == data[i][0]:
            val=data[i][1]
            return val
    for i in range(len(data)-1):
        if(x-data[i][0])*(x-data[i+1][0])<0: #this means x belongs to (xi,x(i+1))
            val=data[i][1]
            return val
        elif(x>data[-1][0]):  #last interval must be done separately
            val=data[-1][1]
            return val
        
#for i in range(-20,50):
  #x=0.1*i  
  #print( x,piecewise(x, dat))

def test_piecewise():
    """Test using the piecewise floor function, in (0,5)"""
    dat=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
    for i in range(0,555):
        x=0.01*i
        value=piecewise(x, dat)
        expect=floor(x)
        success=abs(value-expect)<1e-14
        msg="test fails for x=%.2f in floor function" %x
        assert success, msg
        
test_piecewise()


def plot_piecewise(data, xmax):  #data=[(xi,vi)]
    x=np.linspace(data[0][0],xmax,501)
    y=np.zeros_like(x)
    for i in range(len(x)): #piecewise is not vectorized yet
        y[i]=piecewise(x[i],data)
    
    plt.plot(x,y,"r:")
    plt.plot(x,y,"ro", markersize=2 )
    plt.title("Piecewise function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig('ej5.47pw.png')

plot_piecewise(dat, 3)
        
    
