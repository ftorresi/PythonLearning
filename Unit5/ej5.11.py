import sys
import numpy as np
import matplotlib.pyplot as plt

def y(t, v0=10, g=9.81):
    return v0*t-0.5*g*t**2


v0_list=[]
#read v0 from command line
for i in range(1,len(sys.argv)):
    v0_list.append(float(sys.argv[i]))
    
g=9.81

for v0 in v0_list:
    tmax=2.*v0/g
    t=np.linspace(0,tmax,100)
    h=y(t, v0)
    plt.plot(t, h, label="v0=%g" %v0 )
    plt.legend()

plt.axis([-0.02, 2.*max(v0_list)/g, 0, 1.02*y(max(v0_list)/g,max(v0_list))]) # [tmin, tmax, ymin, ymax]
plt.xlabel("time [s]")
plt.ylabel("height [m]")
plt.title("h(t) for several v0s")
plt.savefig("ej5.11ht.png")
plt.show()
