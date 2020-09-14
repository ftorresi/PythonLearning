import random
#OBS: The Hint given is not correct, since it's impossible to have m>7.
# The worst case would be to obtain 1,2,3,4,5,6, after which the game is won with m=7.
# So the maximum m is 7 with p(m=7)=1/6**6.

def throw_dice():
    d=random.randint(1, 6)
    return d

def compute_prob(N=None):
    if N==None:
        N = int(input('How many experiments? '))
    mfreq=[0]*6 #frequencies of m, from 2 to 7
    for i in range(N):
        m=2 #Initially, 2 dice are thrown
        d1=throw_dice()
        d2=throw_dice()
        while(d2>d1):
            m+=1
            d1=d2
            d2=throw_dice()
        mfreq[m-2]+=1
    for i in range(len(mfreq)):
        #print(f)
        mfreq[i]/=N #Get prob of getting that m
        #print(f)
    return mfreq
            
mf=compute_prob()
print("Probability p of needing m throws:") 
for i in range(len(mf)):
    print("m=%i, p=%g%%" %(i+2,100*mf[i]))
print("NOTE: The exact probability of m=2 is 58.33% and for m=7 is 0.002%") 

print("If you pay 1 euro to play, the fair amount to get paid when winning after m or less throws is:") 
for i in range(len(mf)):
    print("m=%i, money=%g euro" %(i+2,1/sum(mf[:i+1])))
    
print("If you pay 1 euro to play, the fair amount to get paid when winning in exactly m throws is:") 
for i in range(len(mf)):
    if mf[i]!=0: print("m=%i, money=%g euro" %(i+2,1/mf[i]))
    else: print("m=%i was not obtained in this run" %(i+2))
