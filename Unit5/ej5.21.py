import numpy as np
import matplotlib.pyplot as plt
import sys



try:
    dt=float(sys.argv[1])
except IndexError:
    print("Need dt>0 as argument")
    sys.exit(1)
if dt<=0:
    raise ValueError("dt must be positive")

#Since we need to load the whole file, and it's tabular data we use np.loadtxt   
# Read table of floats
a = np.loadtxt("acc_data-ej20.dat", dtype=np.float) #it's only one column

v=np.zeros_like(a) #velocity array

for i in range(1,v.size): #v[0]=0
    v[i]=v[i-1]+0.5*dt*(a[i-1]+a[i])

print(v)

#Let's plot a and v
t=np.linspace(0,dt*v.size,v.size)
plt.figure()
plt.plot(t,a, "k-",label='acceleration')
plt.plot(t,v, "r-.",label='velocity')
plt.legend()
plt.xlabel("t [s]")
plt.ylabel("v and a [m/s and m/s2]")
plt.title("Velocity from acceleration via trapezoidal rule, dt=%g s" %dt)
plt.show()
