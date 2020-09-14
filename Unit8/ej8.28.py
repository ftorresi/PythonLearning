import numpy as np

N = int(input('How many experiments? '))
r = float(input('Money received when winning? '))

money=0
for i in range(N):
    #d1=np.random.random_integers(1,6,size=4)
    #s=np.sum(d1)
    s=np.sum(np.random.random_integers(1,6,size=4)) #shorter expr. Even shorter if replace s<9 for the np.sum expression
    if s<9: money+=r-1
    else: money-=1
net=money/N
print("Net money won per game: %g" %net)

#For the game to be fair, the reward per game won should be about €18.5 (probability of winning is approx. 5.4%, according to ex. 8.9)
