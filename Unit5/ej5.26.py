import numpy as np
import matplotlib.pyplot as plt

def p_L(x, xp, yp):
    pL=0.0
    xp=np.asarray(xp)
    yp=np.asarray(yp)
    if not xp.size == yp.size:
        print("Both data arrays must have the same size")
    else:
        for k in range(xp.size):
            pL+=yp[k]*L_k(x, k, xp, yp)
        return pL
    
    
    
def L_k(x, k, xp, yp):
    Lk=1.0
    for i in range(xp.size):
        if i != k:
            Lk*=(x-xp[i])/(xp[k]-xp[i])
    return Lk


def graph(f, n, xmin, xmax, resolution=1001):
    xval=np.linspace(xmin,xmax,n) #interpolation points
    yval=f(xval)
    
    xplot=np.linspace(xmin,xmax,resolution) #plotting points
    yplot=p_L(xplot, xval, yval)
    
    plt.figure()
    plt.plot(xplot,yplot, "r-", label='interpolation polynomial' )
    plt.plot(xval,yval, "bo", markersize=3, label='Interpolation Points' )
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interpolation of %s using %d uniformly distributed points \n between %g and %g" %(f.__name__,n,xmin,xmax))
    plt.savefig("ej5.26Lp.png")
    plt.show()
    
    
def sine(x):
    return np.sin(x)

graph(sine, 5, 0, np.pi)


