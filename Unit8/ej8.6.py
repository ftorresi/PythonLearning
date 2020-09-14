import random
def throw_dice():
    d=random.randint(1, 6)
    return d

M = int(input('How many experiments? '))
n = int(input('How many dice? '))
s=0
for i in range(M):
    for j in range(n):
        r=throw_dice()
        if r==6:
            s+=1
            break #don't throw more dice if a 6 was obtained
print("Probability of getting a 6 when rolling %g a dice:%g%%" %(n,100.*s/M)) 
    
