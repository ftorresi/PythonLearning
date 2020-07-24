import numpy as np

def h(x):
    return np.exp(-0.5*x**2)/np.sqrt(2*np.pi)

x=np.linspace(-4,4,41)
y=h(x)

for i in range(41):
    print x[i], y[i]
