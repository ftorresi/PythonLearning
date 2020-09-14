def etabar(t,per,A=1):
    n=A*numpy.sin(2*t*numpy.pi/per)
    return n
    
def noisify(arr):
    A=numpy.max(arr)
    eps=numpy.random.normal(0,0.04*A,len(arr))
    arr=arr+eps
    return arr,eps

def der(arr,t):
    d=(arr[2:]-arr[:-2])/(2*(t[2:]-t[:-2]))
    return d

def d2(arr,t):
    d=(arr[2:]-2*arr[1:-1]+arr[:-2])/((t[2:]-t[:-2])*(t[2:]-t[:-2]))
    return d



    
    
#Main program
import numpy
import matplotlib.pyplot as plt
p=2*numpy.pi
t=numpy.linspace(0,5*p,201)
etabar=etabar(t,p)
eta,noise=noisify(etabar)
meanE=numpy.sum(noise)/len(noise)
sdE=numpy.sqrt(numpy.sum(noise*noise)/len(noise)-meanE**2)
print("Mean noise: %7.4g, noise standard deviation: %7.4g"%(meanE,sdE))

detabar=der(etabar,t)
#deta=der(eta,t)
dE=der(noise,t)
meandE=numpy.sum(dE)/len(dE)
sddE=numpy.sqrt(numpy.sum(dE*dE)/len(dE)-meandE**2)
print("Mean noise derivative: %7.4g, noise derivative standard deviation: %7.4g"%(meandE,sddE))

d2etabar=d2(etabar,t)
d2E=d2(noise,t)
meand2E=numpy.sum(d2E)/len(d2E)
sdd2E=numpy.sqrt(numpy.sum(d2E*d2E)/len(d2E)-meand2E**2)
print("Mean noise second derivative: %7.4g, noise second derivative standard deviation: %7.4g"%(meand2E,sdd2E))
print("Conclusion: When derivatives are calculated, the standar deviation of the noise increases, making such derivatives more noisy and innacurate than the original values")


plt.figure()
plt.plot(t,etabar,"r-",label="etabar")
plt.plot(t,eta,"bo",label="eta")
plt.plot(t,noise,"g--",label="noise")
plt.legend()
plt.savefig("ej8.45eta.png")

plt.figure()
plt.plot(t[1:-1],detabar,"r-",label="d(etabar)/dt")
#plt.plot(t[1:-1],deta,"co",label="d(eta)/dt")
plt.plot(t[1:-1],(detabar+dE),"bo",label="d(eta)/dt")
plt.plot(t[1:-1],dE,"g--",label="d(noise)/dt")
plt.legend()
plt.savefig("ej8.45deta.png")

plt.figure()
plt.plot(t[1:-1],d2etabar,"r-",label="d2(etabar)/dt2")
#plt.plot(t[1:-1],deta,"co",label="d(eta)/dt")
plt.plot(t[1:-1],(d2etabar+d2E),"bo",label="d2(eta)/dt2")
plt.plot(t[1:-1],d2E,"g--",label="d2(noise)/dt2")
plt.legend()
plt.savefig("ej8.45d2eta.png")
#plt.show()
