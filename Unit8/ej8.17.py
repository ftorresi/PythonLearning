import numpy as np

def interval_prob(N,a=0.5,b=0.6):
    """Probability of get a number in [a,b] for 0<=a<b<1"""
    r=np.random.rand(N)
    r=r[r>=0.5] #from r, keep values greater or eq to 0.5
    r=r[r<=0.6] #then keep only lowereq to 0.6
    M=len(r)
    return float(M/N)


Nlist=[10**k for k in (1,2,3,6)]

print("Probability p of getting a number in [0.5,0.6] \nwhen drawing uniformly distributed random numbers from [0,1)")
for n in Nlist:
    p=interval_prob(n)
    print("N=%i, p=%g" %(n,p))

