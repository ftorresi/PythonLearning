import random
def throw_dice():
    d=random.randint(1, 6)
    return d

###Part a: expected p=1/6=16.6666%
N = int(input('How many experiments? '))
s=0
for i in range(N):
    r=throw_dice()
    if r==6: s+=1
print("Probability of getting a 6 when rolling a dice:%g%%" %(100.*s/N)) 
    
###Part b: expected p=1/6**4=0.07716 %
s=0
for i in range(N):
    r1=throw_dice()
    r2=throw_dice()
    r3=throw_dice()
    r4=throw_dice()
    if(r1==6 and r2==6 and r3==6 and r4==6): s+=1
print("Probability of getting four 6 when rolling four dice:%g%%" %(100.*s/N)) 

###Part c: expected p=1/6=16.6666%
s=0
m=0
for i in range(N):
    r1=throw_dice()
    if r1==6:
        r2=throw_dice()
        if r2==6:
            r3=throw_dice()
            if r3==6:
                m+=1 #I got the 3 first 6s
                r4=throw_dice()
                if r4==6: s+=1  #got last 6
print("Probability of getting a 4th 6 having previously obtained 3 6s:%g%%" %(100.*s/m)) 
