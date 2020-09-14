import sys
import random, numpy

try:
    np = int(sys.argv[1]) #num. of particles
    ns = int(sys.argv[2]) #num. of steps
    r = float(sys.argv[3])  #probability of going to the right
except IndexError:
    np = 4     # no of particles
    ns = 100   # no of steps
    r=0.5      #probability of going to the right


xmax = numpy.sqrt(ns); xmin = -xmax    # initial extent of plot axis
positions = numpy.zeros(np)            # all particles start at x=0

y = positions.copy()                   # y position is always 0

for step in range(ns):
    for p in range(np):
        coin = random.random()
        if coin < r:
            positions[p] += 1   # one unit length to the right
        else:
            positions[p] -= 1   # one unit length to the left

avg=sum(positions)/np #average position
expected=r*ns-(1-r)*ns
print("Computed average position after %i steps: %g, expected: %g"%(ns, avg, expected))
