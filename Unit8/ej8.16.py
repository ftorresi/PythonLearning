import numpy as np
N=int(input("How many experiments? "))
ran=np.random.rand(N)
coin=np.where(ran<=0.5,1,0)
nt=np.sum(coin) #number of tails
ntp=100*nt/N
print("Total number of coins: %i, i.e. %5.2f%%" %(nt,ntp))
