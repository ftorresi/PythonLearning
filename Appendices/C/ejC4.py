import numpy as np
import matplotlib.pyplot as plt

def odesolve(x0, xf, h, a, u0):
    """Solve numerically u'=a*u"""
    x=np.linspace(x0,xf,1+int((xf-x0)/h))
    u=np.zeros(len(x))
    u[0]=u0
    for i in range(1,len(x)):
        u[i]=u[i-1]*(1+a*h)
    return x,u

def u(x,a):
    return np.exp(a*x)

x0=0
xf=40
a=-1
u0=1
steps=[1.1,1.5,1.9,2.1] #we expect oscilations for steps>-1/a

xexact=np.linspace(x0,xf,1001)
uexact=u(xexact,a=a)

plt.figure()
plt.plot(xexact,uexact,"k-",label="exact")

for dx in steps:
    xapp, uapp= odesolve(x0=x0, xf=xf, h=dx, a=a, u0=u0)
    plt.plot(xapp,uapp,"-.",label="step=%g"%dx)

plt.legend()
#plt.show()
plt.savefig("ejC4.png")

"""Conclusion: Note that in the ODE solving we have u[i]=u[i-1]*(1+a*h)=u[0]*(1+a*h)**i. 
For a<0 and h>-1/a, a*h<-1 and (1+a*h) is negative so the solution oscilates. Moreover, with a*h>-2, (1+a*h)<-1 and the solution increases in absolute value on each step.
Taking h<-1/a solves the oscilation issue.""" 
