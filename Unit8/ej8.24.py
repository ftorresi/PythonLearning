import numpy as np
from math import factorial as fact

def binomial(x,n,p=0.5):
    coef=fact(n)/(fact(x)*fact(n-x))
    binom=coef*(p**x)*(1-p)**(n-x)
    return binom

def simulate_binomial(p,n,x,N=1000):
    M=0
    for i in range(N):
        r=np.random.rand(n) 
        r=np.where(r<p,1,0) #1=success, 0=failure
        tot=np.sum(r)
        if tot==x: M+=1  #success x times
    b=M/N
    exact=binomial(x,n,p)
    error=abs(b-exact)
    relative_error=error/exact
    return b, error, relative_error

N=100000
n=5
p=0.5
x=2
prob, err, rel= simulate_binomial(p,n,x,N)
print("The probability of getting two heads when flipping a coin five times is approx. %6.3f"%prob)
print("The estimation error is %6.3f, i.e. %6.3f%%\n"%(err,100*rel))

n=4
p=1/6
x=4
prob, err, rel= simulate_binomial(p,n,x,N)
print("The probability of getting four ones in a row when throwing a die is %8.5f"%prob)
print("The estimation error is %8.5f, i.e. %6.3f%%\n"%(err,100*rel))

n=5
p=1/120
x=0 #prob. that the ski won't break
prob, err, rel= simulate_binomial(p,n,x,N) #note that err 
pbreak=1-prob #err is the same, but rel is not
relbreak=err/(pbreak) #actually is approx, but good enough with large enough N

print("The probability of experiencing a ski break in 5 races is %8.5f"%pbreak)
print("The estimation error is %8.5f, i.e. %6.3f%%"%(err,100*relbreak))


