from math import pi, exp, sqrt
import numpy as np

def h(x):
    return exp(-0.5*x**2)/sqrt(2*pi)


n=41
dx=8./(n-1)
x=np.zeros(n)
y=np.zeros(n)
for i in range(len(x)):
    x[i]=-4+i*dx
    y[i]=h(x[i])

for i in range(n):
    print x[i], y[i]
