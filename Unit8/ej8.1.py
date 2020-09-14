import random
N=50
s=0
for i in range(N):
    r = random.randint(0,1)
    s+=r
    if r==0: print("head")
    else: print("tail")
print("%g heads, %g tails" %(N-s,s))
print("%g%% of heads, %g%% of tails" %(100*(N-s)/N,100*s/N))
