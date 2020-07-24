import numpy as np
import matplotlib.pyplot as plt

def c(L, h=50):
    g=9.81
    s=7.9e-2
    rho=1000
    return np.sqrt((g*L/(2*np.pi))*(1+s*(2*np.pi)**2/(rho*g*L**2))*np.tanh(2*h*np.pi/L)) 


x=np.linspace(0.001,0.1,1001)
y=c(x)
plt.figure()
plt.plot(x, y, "-")
#plt.axis([0, 0.105, 2e-4, 1.8e-3])
plt.xlabel("Wavelength [m]")
plt.ylabel("c [m/s]")
plt.title("Speed of surface waves in water, small Wavelength")
#plt.show()


x=np.linspace(1,2000,20000)
y=c(x)
plt.figure()
plt.plot(x, y, "-")
#plt.axis([0, 0.105, 2e-4, 1.8e-3])
plt.xlabel("Wavelength [m]")
plt.ylabel("c [m/s]")
plt.title("Speed of surface waves in water, larger Wavelength")
plt.show()
