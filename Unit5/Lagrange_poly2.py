""" Making ej5.26 a module 
Module containing implementation of Lagrange's interpolation polynomial as well as a ploting such polynomial for a given function, interval and number of sample points."""

import numpy as np
import matplotlib.pyplot as plt
import sys

_filename = sys.argv[0]
_usage = """%s "np.sin(x)", 5, 0, "np.pi" will plot the Lagrange interpolation polynomial p_L for sin(x) in [0,pi] using 5 sample points.
%s test checks for errors in the generation of p_L
""" % (_filename, _filename)

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
    
    plt.plot(xplot,yplot, "o", markersize=1 )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interpolation of %s using %d uniformly distributed points \n between %g and %g" %(f.__name__,n,xmin,xmax))
    #plt.show()
    


def test_p_L():
    xq=np.linspace(0,np.pi,5)
    yq=np.sin(xq)
    for j in range(xq.size): 
        yout=p_L(xq[j], xq, yq)
        assert abs(yout-yq[j])<1e-10, "The polynomial misses some point(s)"
    x0=(xq[1]+xq[2])/2 #trial point in the middle
    y0=np.sin(x0) #exact value
    ylagrange=p_L(x0, xq, yq)
    print("No errors. \nExample: for x=%.3f, sin(x)=%.4f and the interpolated value with 5 equally spaced points in [0, pi] gives %.4f" %(x0,y0,ylagrange))

if __name__ == "__main__":
    if (len(sys.argv) == 2)and(sys.argv[1]=="test"):
        test_p_L()
    
    elif(len(sys.argv) == 5):
        try:
            form=sys.argv[1]
            n=int(sys.argv[2])
            xmin=eval(sys.argv[3])
            xmax=eval(sys.argv[4])
        except:
            print(_usage)
            sys.exit(1)
            
        code=""" \ndef f(x):
            return %s
        """ %form
        exec(code)
        graph(f, n, xmin, xmax)
        plt.show()    
    else:
        print (_usage)


