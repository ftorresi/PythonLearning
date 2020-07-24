import numpy as np
import sys



try:
    dt=float(sys.argv[1])
    k=int(sys.argv[2])
except IndexError:
    print("Need dt>0 and 1<=k<=101 as arguments")
    sys.exit(1)
if dt<=0:
    raise ValueError("dt must be positive")
if not (1<=k<=101):
    raise ValueError("k must be 1<=k<=101")

    
alist=[]
infile=open("ej5.20-acc_data.dat","r")
for i in range(k):
    line=infile.readline()
    alist.append(float(line))
infile.close()
a=np.array(alist)
print(a)

vk=0.5*(a[0]+a[k-1])
for j in range(1,k-1):
    vk+=a[j]
vk*=dt

print("v(%g*dt)=%.3f m/s" %(k,vk))
