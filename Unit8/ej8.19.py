import numpy as np

###Part a
def homogeneous(p,N):
    r=np.random.rand(N)
    r=r[r<p] #Keep only "right" answers, i.e. r<p
    return len(r)/N
    
def homogeneous_ex():
    for p in (0.49,0.51,0.8):
        print("\np=%g" %p)
        for N in (5,1000000):
            print("\nN=%g" %N)
            for i in range(10):
                print(homogeneous(p,N))
#homogeneous_ex()

###Part b:
#Note that gaussian(x,m,s)==(gaussian(x=(x-m)/s,0,1))/s, i.e., given the normal mean zero and unit standard deviation we can easily transform to any mean and deviation
#the cumulative normal distribution can be obtained as phi(x,m,s)=phi((x-m)/s,0,1), and the 2nd one can be obtained from:

from scipy.stats import norm #norm.cdf=cumulative normal distribution with mean zero and unit standard deviation

#Then, phi(N/2,Np,sqrt(Np(p-1))=norm.cdf((0.5-p)/(sqrt(N*p*(1-p))))
import matplotlib.pyplot as plt

p=np.linspace(0.01,0.99,99)
plt.figure()
for N in (5,15,100,1000000):
    y=1-norm.cdf((0.5-p)*np.sqrt(N)/(np.sqrt(p*(1-p))))
    plt.plot(p,y,"-",label="N=%g" %N)


plt.xlabel("prob. of a person giving the right answer")
plt.ylabel("prob. of the majority vote being correct")
plt.legend()
plt.savefig("ej8.19b.png")
###Part c:

def heterogeneous(p,N,s):
    r=np.random.rand(N) 
    pright=np.random.normal(p,s,N) #prob of each person to be correct
    r=r[r<pright] #Keep only "right" answers, i.e. r<p
    return len(r)/N

def heterogeneous_ex():
    for p in (0.49,0.51,0.8):
        print("\np=%g" %p)
        for N in (5,1000000):
            print("\nN=%g" %N)
            for i in range(10):
                print(heterogeneous(p,N,0.2))

#heterogeneous_ex()

###Part d:

def extremes(p):
    smin=0.1
    smax=0.6
    s=np.linspace(smin,smax,51)
    yw=norm.cdf(-p/s) #probability of always being wrong
    yr=1-norm.cdf((1-p)/s) #probability of always being right
    
    plt.plot(s,yw,"x",label="always wrong, p=%g" %p)
    plt.plot(s,yr,"-",label="always right, p=%g" %p)
    plt.legend()

plt.figure()
for p in (0.49,0.51,0.8):
    extremes(p)
plt.xlabel("standard deviation from p of a person giving the right answer")
plt.ylabel("prob. for someone to always be right/wrong")
plt.savefig("ej8.19d.png")

#plt.show()
