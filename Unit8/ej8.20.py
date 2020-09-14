import numpy
import matplotlib.pyplot as plt
def generate(N,seed=0):
    a=8121; c=28411; m=134456; x0=seed #
    r=[]
    for i in range(N):
        x1=(a*x0+c)%m
        y1=x1/m
        r.append(y1)
        x0=x1 #for next step
    return r

N=500000
d=generate(N)
#print(d)    
xmin=0
xmax=1
b=25 #nbins

#Get histo with numpy and then plot as points 
freq,xp=numpy.histogram(d,bins=b,range=(0,1),density=True)
xp+=(xmax-xmin)/(2*(len(xp)-1)) #move representative point of bin to the center
xp=xp[:-1] #delete last 
plt.plot(xp,freq,"o")

#Plot straightforwardly with plt.hist
plt.hist(d, bins=b,range=(0,1),density=True,) #also: bins="auto" range=None (defined automatically) density=False (default, prints frequency instead of density)
plt.title("Density histogram for %i points" %N)
#plt.show()
plt.savefig("ej8.20.png")
