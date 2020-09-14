import random
def throw_dice():
    d=random.randint(1, 6)
    return d

N = int(input('How many experiments? '))
#r = int(input('Money received when winning? '))
d = int(input('How many dice? '))
s = int(input('Limit sum? '))
w=0 #number of winnings
for i in range(N):
    total=0
    for j in range(d):
        total+=throw_dice()
    if total<s:w+=1 
p=w/N
print("Probability of getting a sum less than %i when rolling %i dice: %g" %(s, d, p))
