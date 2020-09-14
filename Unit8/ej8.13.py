###Exercise 8.12 such that the computer and the player can
###use a different number of dice. Let the computer choose a random number of dice
###between 2 and 20. I guess the number of dice is changed on each game, not on each throw, but IDK
import random
import sys

class Dice(object):
    def __init__(self, n=1):
        self.n = n   # no of dice

    def throw(self):
        return [random.randint(1,6) \
                for i in range(self.n)]

class Player(object):
    def __init__(self, name, capital, guess_function, ndice):
        self.name = name
        self.capital = capital
        self.guess_function = guess_function
        self.dice = Dice(ndice)


    def play_one_round(self):
        self.guess = self.guess_function(self.dice.n)
        self.throw = sum(self.dice.throw())
        if self.guess == self.throw:
            self.capital += self.guess
        else:
            self.capital -= 1
        #self.message()
        #self.broke() #Not really needed since nrounds will be played always.

    def message(self):
        print ('%s guessed %d, got %d' %(self.name, self.guess, self.throw))

    def broke(self):
        if self.capital == 0:
            print ('%s lost!' % self.name)

# Guessing strategies
def computer_guess(ndice):
    # Any of the outcomes (sum) is equally likely
    return random.randint(ndice, 6*ndice)

def player_guess(ndice):
    return int(3.5*ndice) #always bet for the most likely outcome: int(7*ndice/2)
    #return int(input('Guess the sum of the no of eyes in the next throw: '))

def play(nrounds, ndicemachine=2, ndiceplayer=2):
    player = Player('YOU', nrounds, player_guess, ndiceplayer)
    computer = Player('Computer', nrounds, computer_guess, ndicemachine)

    for i in range(nrounds):
        player.play_one_round()
        computer.play_one_round()
        #print ('Status: user has %d euro, machine has %d euro\n' %(player.capital, computer.capital))
        if player.capital == 0 or computer.capital == 0:
            break  # terminate game

    mw=0
    pw=0
    if computer.capital > player.capital:
        winner = 'Machine'
        mw=1
    elif computer.capital == player.capital:
        winner = 'Nobody'
    else:
        winner = 'You'
        pw=1
    #print (winner, 'won!')
    return mw, pw

machinewins=0
playerwins=0
N=10000
for i in range(N):
    nmach=random.randint(2,20)
    nplay=nmach
    mw,pw=play(nrounds=25, ndicemachine=nmach, ndiceplayer=nplay)
    machinewins+=mw
    playerwins+=pw
mp=100*machinewins/N
pp=100*playerwins/N
print("\nPlaying with the same number of dice as the machine and betting for the most likely outcome 7*ndice/2...")
if(mp>pp):
    print("Your strategy didn't beat the machine, it won %g%% of the times vs your %g%%"%(mp,pp))
else:
    print("Your strategy beat the machine, you won %g%% of the times vs its %g%%"%(pp,mp))
    
playerwins=0    
machinewins=0
N=10000
for i in range(N):
    nplay=5 #Let's suppose we have to choose before the machine
    nmach=random.randint(2,20)
    mw,pw=play(nrounds=25, ndicemachine=nmach, ndiceplayer=nplay)
    machinewins+=mw
    playerwins+=pw
mp=100*machinewins/N
pp=100*playerwins/N
print("\nPlaying with 20 dice and betting for the most likely outcome 7*ndice/2...")
if(mp>pp):
    print("Your strategy didn't beat the machine, it won %g%% of the times vs your %g%%"%(mp,pp))
else:
    print("Your strategy beat the machine, you won %g%% of the times vs its %g%%"%(pp,mp))
    
playerwins=0
machinewins=0
N=10000
for i in range(N):
    nplay=random.randint(2,20) #Let's suppose we have to choose before the machine
    nmach=random.randint(2,20)
    mw,pw=play(nrounds=25, ndicemachine=nmach, ndiceplayer=nplay)
    machinewins+=mw
    playerwins+=pw
mp=100*machinewins/N
pp=100*playerwins/N
print("\nPlaying with random number of dice and betting for the most likely outcome 7*ndice/2...")
if(mp>pp):
    print("Your strategy didn't beat the machine, it won %g%% of the times vs your %g%%"%(mp,pp))
else:
    print("Your strategy beat the machine, you won %g%% of the times vs its %g%%"%(pp,mp))

print("Conclusion: always bet for int(3.5*ndice)")
