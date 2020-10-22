import numpy as np
import matplotlib.pyplot as plt

def odesolve(x0, xf, h, alpha, u0):
    """Solve numerically u'(x)=alpha(x)*u(x)"""
    x=np.linspace(x0,xf,1+int((xf-x0)/h))
    u=np.zeros(len(x))
    u[0]=u0
    for i in range(1,len(x)):
        u[i]=u[i-1]*(1+alpha(x[i-1])*h)
    return x,u

def umean(x,a,b,xf):
    return np.exp((a-0.5*b*xf)*x)

def uexact(x,a,b,x0,u0):
    c=np.log(u0)-a*x0+0.5*b*x0**2
    return np.exp((a*x-0.5*b*x**2+c))

x0=0
xf=10
a=1
b=0.1
u0=1
steps=[0.01,0.1,1]
alpha = lambda t: a-b*t

xexact=np.linspace(x0,xf,1001)
uexact=uexact(xexact,a=a,b=b,x0=x0,u0=u0)
uavg=umean(xexact,a=a,b=b,xf=xf)

plt.figure()
plt.plot(xexact,uexact,"k-",label="exact solution")
plt.plot(xexact,uavg,"k:",label="mean alpha value")


for dx in steps:
    xapp, uapp= odesolve(x0=x0, xf=xf, h=dx, alpha=alpha, u0=u0)
    plt.plot(xapp,uapp,"-.",label="step=%g"%dx)

plt.legend()
#plt.show()
plt.savefig("ejC5.png")

