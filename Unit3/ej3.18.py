from math import sqrt, sin, cos, pi

def pathlength(x, y):
    if len(x)!=len(y):
        print "both argumets must have the same number of elements!"
        return
    else:
      leng=0.0
      for i in range(1,len(x)):
          leng+=sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
      return leng

def pointgen(n):
    """generates a set of n+1 points on a circumference with radius 1/2"""
    x=[0.5*cos(2*pi*i/n) for i in range(n+1)]
    y=[0.5*sin(2*pi*i/n) for i in range(n+1)]
    return x, y

for k in range(2,11):
    n=2**k
    xk, yk = pointgen(n)
    lenk=pathlength(xk, yk)
    print "for n=%-4d, pi=%.6f, error=%.6f" %(n, lenk, abs(pi-lenk))
