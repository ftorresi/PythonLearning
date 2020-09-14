#As the description of the game is not completely clear, i'm assumming that the player 
#makes all the guesses and at the end it's informed of the results

def simulate(m,n,p,q,b):
    beer=numpy.random.random(n) #guesses
    r=numpy.sum(numpy.where(beer<b,1,0))
    net_money=-p*n+q*r
    return net_money, r


#Main program
import numpy
N=int(input("Number of experiments? "))
cash=0
full=0
for i in range(N):
    money, r= simulate(4,4,3,6,0.25)
    cash+=money
    if r==4: full+=1 #all correct
money_per_game=cash/N
full_prob=full/N
print("Paying 3 per guess, winning 6 per right guess, with a winning prob of 0.25:")
print("The average earning per game is %6.3f" %money_per_game)
print("The probability of guessing all brands is %6.4f" %full_prob)

cash=0
full=0
for i in range(N):
    money, r= simulate(4,4,3,6,0.5)
    cash+=money
    if r==4: full+=1 #all correct
money_per_game=cash/N
full_prob=full/N
print("\nDoubling the winning prob to 0.5:")
print("The average earning per game is %6.3f" %money_per_game)
print("The probability of guessing all brands is %6.4f" %full_prob)
