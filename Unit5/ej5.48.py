from math import floor #to use in test
import numpy as np
import matplotlib.pyplot as plt

dat=[(0,-1),(1,0),(1.5,4),(2,3)] 

def piecewise_vec(x, data, xmax): #data=[{(xi,vi)}]
    x=np.asarray(x)
    err=np.logical_and(x>=data[0][0],x<=xmax) #boolean array, same len as x, check all values are greater than the minimum and smaller than the maximum
    if not err.all(): #if err aren't all True:
        print (" All arguments must be greater than or equal to %.2f and smaller than or equal to %.2f" %(data[0][0],xmax) )
        return None
    r=np.zeros_like(x)
    for i in range(len(data)-1):
        condition=np.logical_and(x>=data[i][0],x<data[i+1][0])
        r[condition]=data[i][1]
    condition=np.logical_and(x>=data[-1][0], x<=xmax) #last interval must be done separately
    r[condition]=data[-1][1]
    return r
        
#x=np.linspace(-0,5,51)
#print (piecewise_vec(x, dat,5))

def test_piecewise_vec():
    """Test using the piecewise floor function, in (0,5)"""
    dat=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
    for i in range(0,555):
        x=0.01*i
        value=piecewise_vec(x, dat,6)
        expect=floor(x)
        success=abs(value-expect)<1e-14
        msg="test fails for x=%.2f in floor function" %x
        assert success, msg
        
#test_piecewise_vec()


def plot_piecewise_vec(data, xmax):  #data=[(xi,vi)]
    x=np.linspace(data[0][0],xmax,501)
    y=piecewise_vec(x,data,xmax)
    
    plt.plot(x,y,"r:")
    plt.plot(x,y,"ro", markersize=2 )
    plt.title("Vectorized piecewise function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig('ej5.48pw.png')

plot_piecewise_vec(dat, 3)
