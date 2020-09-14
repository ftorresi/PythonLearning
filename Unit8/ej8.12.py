 
"""
Class version of ndice1.py.
"""
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
    return 7 #always bet for the most likely outcome (for 2 dice)
    #return int(input('Guess the sum of the no of eyes in the next throw: '))

def play(nrounds, ndice=2):
    player = Player('YOU', nrounds, player_guess, ndice)
    computer = Player('Computer', nrounds, computer_guess, ndice)

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
N=100000
for i in range(N):
    mw,pw=play(nrounds=25, ndice=2)
    machinewins+=mw
    playerwins+=pw
mp=100*machinewins/N
pp=100*playerwins/N
print("Playing with 2 and betting for the most likely outcome, 7;")
if(mp>pp):
    print("your strategy didn't beat the machine, it won %g%% of the times vs your %g%%"%(mp,pp))
else:
    print("your strategy beat the machine, you won %g%% of the times vs its %g%%"%(pp,mp))
