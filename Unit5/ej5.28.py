import numpy as np
import matplotlib.pyplot as plt

def f(x,t=0):
    return np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))

x=np.linspace(-4,4,800)
y=f(x,0)
plt.figure()
plt.plot(x, y, "-",label='t=0')
plt.legend()
plt.axis([-4.1, 4.1, -1, 1])
plt.xlabel("x")
plt.ylabel("f(x,t)")
plt.title("Wave packet")
plt.show()
