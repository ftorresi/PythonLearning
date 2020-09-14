import random
from math import sqrt
def draw_ball(hat):
    """Draw a ball using list index."""
    index = random.randint(0, len(hat)-1)
    color = hat.pop(index)
    return color, hat

def new_hat():
    colors = 'green', 'red', 'yellow', 'brown'   # (tuple of strings)
    colorsfreq=3,5,5,7 #number of balls of each color
    hat = []
    for color,f in zip(colors,colorsfreq):
        for i in range(f):
            hat.append(color)
    return hat

N =int(input('How many experiments? '))
wintable=[[0 for j in range(4)] for i in range(7)] #number of wins on each combination, wintable[i][j]=i+4 balls,option j+1
cashtable=[[0 for j in range(4)] for i in range(7)] #money won for each combination

def checkwin(balls): #check winning and add cash win/loses.
    n=len(balls)
    
    if balls.count('red') == 3:
        wintable[n-4][0]+=1
        cashtable[n-4][0]+=60
    else: cashtable[n-4][0]-=2*n
    #not using elif since 2 or more options may be winning options for the same set of balls 
    #ex.:r r r b b b y g will win in options 1,2 and 4
    
    if balls.count('brown') >= 3:
        wintable[n-4][1]+=1
        cashtable[n-4][1]+=7+5*sqrt(n)
    else: cashtable[n-4][1]-=2*n
    
    if balls.count('brown') == 1 and balls.count('yellow') == 1:
        wintable[n-4][2]+=1
        cashtable[n-4][2]+=n**3-26
    else: cashtable[n-4][2]-=2*n
    
    if balls.count('brown') > 0 and balls.count('yellow') > 0 and balls.count('red') > 0 and balls.count('green') > 0:
        wintable[n-4][3]+=1
        cashtable[n-4][3]+=23
    else: cashtable[n-4][3]-=2*n
    
    

## Run experiments

for e in range(N):
    hat = new_hat()
    balls = []           # the n balls we draw
    for i in range(10):  #draw 10 balls
        color, hat = draw_ball(hat)
        balls.append(color)    
        if i>2: checkwin(balls)  #check wins from 4 to 10 balls (i=3 means 4 balls)


#Normalize per number of experiments
wt=[[100*el/N for el in ball]for ball in wintable]
ct=[[el/N for el in ball]for ball in cashtable]

print("The % probability of winning for n balls and game option g are:")
print("n   g=1     g=2     g=3     g=4")
for i in range(7):
    print("%-2i  %-6.2f  %-6.2f  %-6.2f  %-6.2f" %(i+4,wt[i][0],wt[i][1],wt[i][2],wt[i][3]) )
    
print("\nThe net money earned for n balls and game option g is:")
print("n     g=1     g=2     g=3     g=4")
for i in range(7):
    print("%-2i  %6.2f  %6.2f  %6.2f  %6.2f" %(i+4,ct[i][0],ct[i][1],ct[i][2],ct[i][3]) )


print("Gametype 3 is preferred for 4 and 5 balls")
print("For 6 or more balls, gametype 4 gives the best money")
print("The optimal choice for the long run would be gametype 4 and 10 balls")

