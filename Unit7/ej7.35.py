import sys
import numpy as np

conditions=[]
for i in range(len(sys.argv[1:-2])):
    conditions.append(eval(sys.argv[1+i]))
    
p,q=float(sys.argv[-2]),float(sys.argv[-1])

horizontal=[]
for i in range(len(conditions)):
    if conditions[i][0]==0:
        horizontal.append(conditions[i])

for elem in horizontal:
    conditions.remove(elem) #remove horizontal cond.
    
vertical=[]
for i in range(len(conditions)):
    if conditions[i][1]==0:
        vertical.append(conditions[i])

for elem in vertical:
    conditions.remove(elem) #remove vertical cond.
print (horizontal)
print (vertical)
print (conditions)

# for this to give a nice plot, it should be x>0, y>0
xmax=max([conditions[i][2]/conditions[i][0] for i in range(len(conditions))])
ymax=max([conditions[i][2]/conditions[i][1] for i in range(len(conditions))])
#print (xmax)
#print (ymax)

import matplotlib.pyplot as plt
y=np.linspace(0,ymax,2)
for elem in vertical:
    x=(elem[2]-elem[1]*y)/elem[0]
    plt.plot(x,y,"-")
x=np.linspace(0,xmax,2)
for elem in conditions:
    y=(elem[2]-elem[0]*x)/elem[1]
    plt.plot(x,y,"-")
for elem in horizontal:
    y=(elem[2]-elem[0]*x)/elem[1]
    plt.plot(x,y,"-")

for a in [0,100,200,300,400,500,600,700,800]:
    y=a/q-(p/q)*x
    plt.plot(x,y,":", label=a)

a=720 #optimal revenue, for x=16 and y=0 
y=a/q-(p/q)*x
plt.plot(x,y,"r-", label="optimal reveue: %g"%a)
plt.legend()

plt.show()

