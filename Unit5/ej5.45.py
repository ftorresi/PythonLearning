import numpy as np
import matplotlib.pyplot as plt
import sys


try: 
    m=float(sys.argv[1])
except IndexError:
    print ("Particle's mass must be provided")
    m=float(input("m [kg]=?"))
    
try: 
    v0=float(sys.argv[2])
except IndexError:
    print ("Initial velocity must be provided")
    v0=float(input("v0 [m/s]=?"))

g = 9.81
    
def y(t):
    return v0*t - 0.5*g*t**2
    
def v(t):
    return v0-g*t

def K(t):
    return 0.5*m*(v(t))**2
    
def P(t):
    return m*g*y(t)

tmax=2*v0/g 
tlist=np.linspace(0,tmax,501)
kinen=K(tlist)
poten=P(tlist)
toten=kinen+poten

plt.plot(tlist,toten,"k-", label="Total Energy")
plt.plot(tlist,kinen,"r-", label="Kinetic Energy")
plt.plot(tlist,poten,"b-", label="Potential Energy")
plt.axis([-.01*tmax,1.01*tmax,-0.02*toten[0],1.02*toten[0]])
plt.legend()
plt.xlabel("t [s]")
plt.ylabel("E [J]")
plt.title("Energy on a vertical throw for m=%.1f kg and v0=%.1f m/s" %(m,v0))
plt.savefig('ej5.45.png')
plt.show()

