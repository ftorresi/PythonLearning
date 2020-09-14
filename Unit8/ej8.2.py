import random

def interval_prob(N,a=0.5,b=0.6):
    """Probability of get a number in [a,b] for 0<=a<b<1"""
    M=0
    for i in range(N):
        r=random.random()
        if a<=r<=b:
            M+=1
    return float(M/N)

Nlist=[10**k for k in (1,2,3,6)]

print("Probability p of getting a number in [0.5,0.6] \nwhen drawing uniformly distributed random numbers from [0,1)")
for n in Nlist:
    p=interval_prob(n)
    print("N=%i, p=%g" %(n,p))

