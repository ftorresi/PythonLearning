import numpy as np
import matplotlib.pyplot as plt

def h(x):
    return np.exp(-0.5*x**2)/np.sqrt(2*np.pi)

x=np.linspace(-4,4,41)
y=h(x)

plt.figure()
plt.plot(x, y, "-")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Gaussian function with s=1, m=0" ])
plt.axis([-4.05, 4.05, -0.05, 0.4]) # [tmin, tmax, ymin, ymax]
plt.title("Exercise 5.4")
#plt.savefig("ej5.4.pdf") # produce PDF
#plt.savefig("ej5.4.png") # produce PNG
plt.show()
