import numpy as np
import matplotlib.pyplot as plt

def odesolve(x0, xf, h, y0):
    """Solve numerically dy/dx=1/(2*(y-1))"""
    x=np.linspace(x0,xf,1+int((xf-x0)/h))
    y=np.zeros(len(x))
    y[0]=y0
    for i in range(1,len(x)):
        y[i]=y[i-1]+h/(2*(y[i-1]-1))
    return x,y

def y(x,eps):
    return 1+np.sqrt(x+eps)

x0=0
xf=4
eps=1e-3
y0=1+np.sqrt(eps)
steps=[1,0.25,0.01]

xexact=np.linspace(x0,xf,1001)
yexact=y(xexact,eps=eps)

plt.figure()
plt.plot(xexact,yexact,"k-",label="exact")

for dx in steps:
    xapp, yapp= odesolve(x0=x0, xf=xf, h=dx, y0=y0)
    plt.plot(xapp,yapp,"-.",label="step=%g"%dx)

plt.legend()
plt.savefig("ejC3.png")

"""Conclusion: Note that in the ODE solving we have a term h/2*eps for y[1]. When eps~0, if h is not small enough, such term gives a huge value for y[1], moving the approximate solution very far from the exact result.""" 
