def random_walk_2D(np, ns, xmin=None, xmax=None, ymin=None, ymax=None):
    xpositions = numpy.zeros(np)
    ypositions = numpy.zeros(np)
    if xmin==None: xmin=-ns
    if ymin==None: ymin=-ns
    if xmax==None: xmax=ns
    if ymax==None: ymax=ns

    for step in range(ns):
        #print(xpositions, ypositions)
        for i in range(np):
            direction = random.randint(1, 4)
            if direction == 1:
                if ypositions[i]<ymax: #move only if it's under ymax
                    ypositions[i] += 1
            elif direction == 2:
                if ypositions[i]>ymin: #move only if it's abovea ymin
                    ypositions[i] -= 1
            elif direction == 4:
                if xpositions[i]<xmax: #move only if it's left xmax
                    xpositions[i] += 1
            elif direction == 3:
                if xpositions[i]>xmin: #move only if it's right xmin
                    xpositions[i] -= 1
    return xpositions, ypositions

# main program:
import random
#random.seed(10)
import sys
import numpy

np        = int(sys.argv[1])  # number of particles
ns        = int(sys.argv[2])  # number of steps
x,y=random_walk_2D(np, ns, -1, 1, -1, 1)
print (x,y)
