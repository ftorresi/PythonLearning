import numpy as np

###Part a:

def coinflip(N):
    """Flip a coin N times"""
    r=np.random.rand(N)
    r=np.where(r<0.5,1,0) #1=head, 0=tail
    return r

#print(coinflip(10))


###Part b:
def headprob(M,r):
    n=np.sum(r[:M])
    return n/M

N=1000    
c=coinflip(N)
for N1 in (10,100,500,1000):
    print("In %i experiments, the prob. of getting a head is %g  " %(N1,headprob(N1,c)))

###Part c:

def probevol(c):
    N=len(c)
    p = np.zeros(N)
    for i in range(N):
        p[i] = np.sum(c[:i+1])/float(i+1)
    return p
#print(probevol(c))

###Part d:

def probevol2(c):
    N=len(c)
    q = np.cumsum(c) #array q[i]=np.sum(c[:i+1])
    I= np.arange(1,N+1) #array with integers from 1 to n
    p = q/I
    return p

#print(probevol2(c))

###Part e:
def test_probevol():
    k=coinflip(1000) #test for 1000 values
    p1=probevol(k)
    p2=probevol2(k)
    success= np.allclose(p1,p2)
    assert success, "The functions give different output"

#test_probevol()


###Part f:
import time
t0=time.clock()
probevol(c)
t1=time.clock()
probevol2(c)
t2=time.clock()
trel=(t1-t0)/(t2-t1)
print("For %i flips, the fully vectorized probevol function is %g time faster than the partially vectorized one." %(N,trel))

###Part g:
import matplotlib.pyplot as plt
N=10000
c=coinflip(N)
p=probevol2(c)
I=np.arange(1,N+1)
plt.plot(I,p,"bo", markersize=2)
plt.title("Estimation of the probability of getting head when flipping a coin")
plt.xlabel("Number of experiments")
plt.ylabel("Estimated probability of getting head")
plt.axis([-0.01*N,1.01*N,0.3,0.7])
#plt.show()
plt.savefig("ej8.23.png")
