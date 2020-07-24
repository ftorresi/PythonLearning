import numpy as np
import matplotlib.pyplot as plt

def mu(T):
    T=T+273.15 #Transform C to K
    A=2.414e-5
    B=247.8
    C=140.0
    return A*10**(B/(T-C)) 

x=np.linspace(0,100,1001)
y=mu(x)
plt.figure()
plt.plot(x, y, "-")
plt.axis([-1, 101, 2e-4, 1.8e-3])
plt.xlabel("temperature [C]")
plt.ylabel("viscosity [Pa s]")
plt.title("Water viscosity")
plt.show()
