from math import pi, sin, cos, sqrt
import sys
import numpy as np
import matplotlib.pyplot as plt

def y(x, v0=10.0, theta=pi/2, y0=0.0):
    g=9.81
    r= x*np.tan(theta)-g*x**2/(2.*(v0*np.cos(theta))**2) + y0
    return r

#read v0, theta and y0 from command line
try:
    v0=float(sys.argv[1])
    theta=eval(sys.argv[2]) #possibility to be given in multiples of pi
    y0=float(sys.argv[3])
except IndexError:
    print("Need arguments v0, theta, y0")
    sys.exit(1)
except ValueError:
    print("v0, y0 must be float; theta may be given in multiples of pi")
    sys.exit(1)

    
g=9.81    
#xmin=v0**2*sin(2*theta)/(2*g)-sqrt(v0**4*(sin(2*theta))**2/(4*g**2)+2*y0*v0**2*(cos(theta))**2/g) #min possible x for y0=0
xmax=v0**2*sin(2*theta)/(2*g)+sqrt(v0**4*(sin(2*theta))**2/(4*g**2)+2*y0*v0**2*(cos(theta))**2/g) #max possible x for y0=0

x=np.linspace(0,xmax,100) #I choose to start from x=0, could use xmin.
h=y(x, v0, theta, y0)

plt.plot(x, h, "bo")
plt.axis([-0.05*xmax, 1.05*xmax, -0.05*np.max(h), 1.05*np.max(h)]) # [tmin, tmax, ymin, ymax]
plt.xlabel("x [m]")
plt.ylabel("height [m]")
plt.title("trajectory for a projectile motion")
plt.savefig("ej5.13xy.png")
plt.show()
