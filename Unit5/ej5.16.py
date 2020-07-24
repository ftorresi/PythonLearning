import matplotlib.pyplot as plt
import sys

try:
    inname=sys.argv[1]
except IndexError:
    print("Need input file name as argument")
    sys.exit(1)

infile=open(inname,"r")

for i in range(4): #skip 4 lines
    infile.readline()
    
x=[]
y=[]
for line in infile:
    data=line.split()
    x.append((data[0]))
    y.append((data[1]))
    
infile.close()

del x[-1] #remove last item
del y[-1] #remove last item

#transform to float
plt.figure()
for i in range(len(x)):
    x[i]=float(x[i])
    y[i]=float(y[i])
    plt.plot(x[i],y[i], "o") #to get different colors for each point.
#plt.axis([1.05*min(x), 1.05*max(x), 0.95*min(y), 1.05*max(y)]) # [tmin, tmax, ymin, ymax]
plt.savefig("ej5.16.png")
plt.show()



