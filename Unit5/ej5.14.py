import numpy as np
import matplotlib.pyplot as plt

infile=open("ej5.14-xy.dat","r")
x=[]
y=[]

for line in infile:
    data=line.split()
    x.append(float(data[0]))
    y.append(float(data[1]))

xa=np.array(x)
ya=np.array(y)

ymin=np.min(ya)
ymax=np.max(ya)
ymean=np.sum(ya)/float(ya.size)
print ("Min. y-value: %.4f" %ymin)
print ("Max. y-value: %.4f" %ymax)
print ("Mean y-value: %.4f" %ymean)

plt.plot(xa, ya, "b-")
plt.axis([1.05*np.min(xa), 1.05*np.max(xa), 1.05*ymin, 1.05*ymax]) # [tmin, tmax, ymin, ymax]
plt.xlabel("x")
plt.ylabel("y")
plt.title("plot of ej5.14-xy.dat")
plt.savefig("ej5.14xy.png")
plt.show()
