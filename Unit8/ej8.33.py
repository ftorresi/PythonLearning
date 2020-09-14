import numpy  # not as np since np is an important variable here
import time, sys

try:
    xp = int(sys.argv[1])  # target
except IndexError:
    xp = 5
    
ns= 10000000 #batch size
position = 0 #Only 1 particle
count=0

# Draw from 1, 2
moves = numpy.random.random_integers(1, 2, size=ns)
# Transform 1 to -1 and 2 to 1
moves = 2*moves - 3

while (position!=xp):
    count+=1
    # Draw from 1, 2
    moves = numpy.random.random_integers(1, 2, size=ns)
    # Transform 1 to -1 and 2 to 1
    moves = 2*moves - 3
    for step in range(ns):
        position += moves[step]
        if position==xp:
            realstep=(count-1)*ns+step+1
            print("Position %i was reached in %i steps" %(xp, realstep))
            break
    if count>100:
        realstep=(count*ns)
        print("More than %i steps. Aborting" %realstep)
        break

###Some results:

#Position 5 was reached in 25 steps
#Position 50 was reached in 11498 steps
#Position 500 was reached in 126536 steps
#Position 5000 was reached in 19639914 steps

