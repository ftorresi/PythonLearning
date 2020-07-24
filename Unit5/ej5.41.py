from math import pi
import numpy as np
import matplotlib.pyplot as plt

#Vectorized S
def S(t,n=10,T=2*pi):
    suma=0.0
    for i in range(1,n+1):
        suma+=(1.0/(2*i-1))*np.sin(2*(2*i-1)*pi*t/float(T))
    suma*=4/np.pi
    return suma

#Vectorized piecewise function    
def fvec(t,T=2*pi):
    condition1=np.logical_and(0<t,t<0.5*T)
    condition2=np.logical_and(0.5*T<t,t<T)
    
    r=np.zeros_like(t)
    r[condition1]=1.0
    r[condition2]=-1.0
    return r
    
T0=2*pi    
tgrid=np.linspace(0,T0,501)
tlist=tgrid[1:-1] #since f(0) and f(T) are not defined
nlist=(1,3,20,200)

y=fvec(tlist,T0)
plt.plot(tlist,y,"k-")
for n in nlist:
    z=S(tlist,n,T0)
    plt.plot(tlist,z,"-.", label="n=%d" %n)
plt.legend()
plt.xlabel("t")
plt.ylabel("S")
plt.title("Step function and its approximations with n sin terms")
plt.savefig('ej5.41.png')
plt.show()

