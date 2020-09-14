import random

def iogen(M,p=0.5):
    s=""
    if p>=0:   #each number depends on the previous 
        r0=random.randint(0,1)
        while(len(s)<M):
            s+=str(r0)
            if random.random()>=p: #Change next number with probability 1-p, otherwise leave it as it is
                r0=1-r0
    else: #p<-0 makes it random
        while(len(s)<M):
            r0=random.randint(0,1)
            s+=str(r0)
    return s
print(iogen(80,-1))  #truly random  
print(iogen(80,0.5))
print(iogen(80,0.8))
print(iogen(80,0.9))
    
