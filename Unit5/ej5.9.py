import numpy as np
import matplotlib.pyplot as plt

def y(t, v0=10, g=9.81):
    return v0*t-0.5*g*t**2

v0=10
g=9.81
tmax=2.*v0/g

t=np.linspace(0,tmax,100)
h=y(t, v0, g)

plt.figure()
plt.plot(t, h, "ro")
plt.xlabel("time [s]")
plt.ylabel("height [m]")
#plt.legend(["legend" ])
plt.axis([-0.02, tmax+0.02, 0, np.max(h)+0.05]) # [tmin, tmax, ymin, ymax]
plt.title("h(t)")
plt.savefig("ej5.9ht.png")
plt.show()
