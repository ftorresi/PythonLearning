import random
def throw_dice():
    d=random.randint(1, 6)
    return d

N = int(input('How many experiments? '))
r = float(input('Money received when winning? '))

money=0
for i in range(N):
    d1=throw_dice()
    d2=throw_dice()
    d3=throw_dice()
    d4=throw_dice()
    s=d1+d2+d3+d4
    if s<9: money+=r-1
    else: money-=1
net=money/N
print("Net money won per game: %g" %net)

#For the game to be fair, the reward per game won should be about €18.5 (probability of winning is approx. 5.4%, according to ex. 8.9)
