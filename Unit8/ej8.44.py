def readfile(inn):
    eta=[]
    with open(inn,"r") as infile:
        for line in infile:
            eta.append(float(line))
    eta=numpy.asarray(eta)
    return eta

            
def plot(p,h,tstart=0,style="-",legend="Unfiltered",xlabel="Time [s]",ylabel="Water height [m]",name="ej8.44eta.png"):
    tval=numpy.arange(tstart,tstart+len(p))*h
    plt.plot(tval,p,style,label=legend)
    plt.legend()
    plt.axis([-0.02*tval[-1],1.02*tval[-1],1.05*min(p),1.05*max(p)])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(name)    
    #plt.show()
    
def vel(p,h):
    v=(p[2:]-p[:-2])/(2*h) #mid-derivative
    return v

def acc(p,h):
    a=(p[2:]-2*p[1:-1]+p[:-2])/(h**2) #mid-second-derivative
    return a
    
def filtre(p):       #Change spelling in order not to confuse with built-in filter
    filt=numpy.ndarray.copy(p)
    filt[1:-1]=0.25*(p[2:]+2*p[1:-1]+p[:-2]) #filt[0]=p[0]; filt[-1]=p[-1]
    return filt

    
#Main program
import numpy, sys    
import matplotlib.pyplot as plt
try:
    h=eval(sys.argv[1])
except:
    h=eval(input("h? "))
eta=readfile("ej8.44.dat")

#unfiltered plots
plt.figure(1)
plot(eta,h)

v=vel(eta,h)
plt.figure(2)
plot(v,h,tstart=1,style="r-",ylabel="Water velocity [m/s]",name="ej8.44vel.png")

a=acc(eta,h)
plt.figure(3)
plot(a,h,tstart=1,style="k-",ylabel="Water acceleration [m/s²]",name="ej8.44acc.png")


#Apply filter
f=0 #filter counter
for N in [1,9,90]: #total filters: 1,10,100
    for i in range(N):
        eta=filtre(eta)
        f+=1
    leg="Filtered %d time(s)" %f
    plt.figure(1)
    plot(eta,h,legend=leg)
    v=vel(eta,h)
    plt.figure(2)
    plot(v,h,tstart=1,legend=leg,ylabel="Water velocity [m/s]",name="ej8.44vel.png")
    a=acc(eta,h)
    plt.figure(3)
    plot(a,h,tstart=1,legend=leg,ylabel="Water acceleration [m/s²]",name="ej8.44acc.png")
