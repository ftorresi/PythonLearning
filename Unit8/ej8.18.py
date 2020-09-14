import numpy as np

def throw7dice(N):
    size=10000  #max. size of batches
    rest=N%size
    batch_sizes = [size]*(N//size) + [rest]
    M=0
    for batch_size in batch_sizes:
        r = np.random.random_integers(1, 6, size=(7, batch_size)) # Throw 7(rows) dice batch_size (columns) times
        s=r.sum(axis=0) #sum on each column
        s=s[s==42] #only interested in all 6, so sum will be 42
        M+=len(s)
    return M/N


Nlist=[10**k for k in (6,7,8)] #In my PC, N=10**8 only works with batches 

print("Probability p of getting seven 6s when throwing 7 dice")
for n in Nlist:
    p=throw7dice(n)
    print("N=%i, p=%g per million" %(n,1e6*p))
print("Theoretical: 3.57 per million")
