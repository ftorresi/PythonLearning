import numpy as np

def picalc(N):
    x=np.random.uniform(-2.0,6.0,N) #square [-2,6]x[-3,5]
    y=np.random.uniform(-3.0,5.0,N)
    d2=(x-2)**2+(y-1)**2
    #print(x)
    #print(y)
    #print(d2)
    inside=len(d2[d2<=16]) #R=4
    return 4*inside/N  #Circle Area/Square Area=pi/4

N = int(input('How many experiments? '))
pi=picalc(N)
print("Estimated value for pi:%g"%(pi))
err=abs(pi-np.pi)
errel=100*err/np.pi
print("Error:%g, i.e. %g%%"%(err, errel))

