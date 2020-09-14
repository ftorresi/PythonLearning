import random
def draw_ball(hat):
    """Draw a ball using list index."""
    index = random.randint(0, len(hat)-1)
    color = hat.pop(index)
    return color, hat

def new_hat():
    colors = 'blue', 'red', 'yellow', 'purple'   # (tuple of strings)
    hat = []
    for color in colors:
        for i in range(10):
            hat.append(color)
    return hat

n =10 # int(input('How many balls are to be drawn? '))
N = int(input('How many experiments? '))

# Run experiments
M = 0  # no of successes
for e in range(N):
    hat = new_hat()
    balls = []           # the n balls we draw
    for i in range(n):
        color, hat = draw_ball(hat)
        balls.append(color)
    if balls.count('blue') == 2 and balls.count('purple')==2:  # exactly 2 blue and 2 purple
        M += 1
print ('Probability of getting 2 blue and 2 purple:', float(M)/N)
