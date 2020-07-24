import numpy as np
import matplotlib.pyplot as plt

xlist=[]
ylist=[]

with open("ej5.22_xy.dat","r") as infile: # Another way to open files
    s=float(infile.readline()) #read s form line 1
    for line in infile:
        data=line.split()
        xlist.append(float(data[0]))
        ylist.append(float(data[1]))
x=np.array(xlist)
y=np.array(ylist)

#y vs x plot
plt.figure()
plt.plot(x,y, "ko-",label='trajectory')
plt.legend()
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Trajectory read from file")
#plt.show()

#!!!!! Task b  !!!!#

def veloc(x,dt): #given an array and dt, return velocity
    v=np.zeros(x.size-1)
    for k in range(v.size):
        v[k]=(x[k+1]-x[k])/float(dt)
    return v

vx=veloc(x,s)
vy=veloc(y,s)
t=np.linspace(0,s*vx.size,vx.size)


#x vs t plot
plt.figure()
plt.plot(t,vx, "ro-",label='vx')
plt.legend()
plt.xlabel("t [s]")
plt.ylabel("vx [m/s]")
plt.title("x-velocity")
#y vs t plot
plt.figure()
plt.plot(t,vy, "bo-",label='vy')
plt.legend()
plt.xlabel("t [s]")
plt.ylabel("vy [m/s]")
plt.title("y-velocity")
plt.show()





