import random

def guessgame(guessfunc):
    number = random.randint(1, 100)
    attempts = 0  # count no of attempts to guess the number
    guess = 0
    p=1; q=100
    while guess != number:
        #guess = eval(input('Guess a number: ')) #now we'll guess automatically
        guess=guessfunc(p,q)
        attempts += 1
        if guess == number:
            #print ('Correct! You used', attempts, 'attempts!')
            return attempts
            break
        elif guess < number:
            p=guess+1
            #print ('Go higher! Number is in [%i,%i]'%(p,q))
        else:
            q=guess-1
            #print ('Go lower! Number is in [%i,%i]'%(p,q))

def guess_midpoint(p,q):
    return int(0.5*(p+q))

def guess_rand(p,q):
    return random.randint(p, q)

mid=0
rnd=0
N=1000000
for i in range(N):
    mid+=guessgame(guess_midpoint)
    rnd+=guessgame(guess_rand) 

mid/=N    
rnd/=N

print("Average attempts for midpoint strategy: %5.2f" %mid)
print("Average attempts for random strategy: %5.2f" %rnd)
if (mid<rnd): print("Midpoint strategy is superior")
else: print("Random strategy is superior")
    
    
    
