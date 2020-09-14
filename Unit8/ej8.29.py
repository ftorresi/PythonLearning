import numpy as np

def picalc(N):
    x=np.random.uniform(-1.0,1.0,N)
    y=np.random.uniform(-1.0,1.0,N)
    d2=x*x+y*y
    #print(x)
    #print(y)
    #print(d2)
    inside=len(d2[d2<=1])
    return 4*inside/N #Circle Area/Square Area=pi/4

N = int(input('How many experiments? '))
pi=picalc(N)
print("Estimated value for pi:%g"%(pi))
err=abs(pi-np.pi)
errel=100*err/np.pi
print("Error:%g, i.e. %g%%"%(err, errel))

