
def random_walk_2D(np, ns, xmin=None, xmax=None, ymin=None, ymax=None):
    if xmin==None: xmin=-ns
    if ymin==None: ymin=-ns
    if xmax==None: xmax=ns
    if ymax==None: ymax=ns
    xpositions = numpy.zeros(np)
    ypositions = numpy.zeros(np)
    moves = numpy.random.random_integers(1, 4, size=ns*np)
    moves.shape = (ns, np)

    for step in range(ns):
        this_move = moves[step,:]
        ypositions += numpy.where(this_move == 1, 1, 0)
        ypositions = numpy.where(ypositions>ymax,ymax,ypositions) #Put back particle inside box
        ypositions -= numpy.where(this_move == 2, 1, 0)
        ypositions = numpy.where(ypositions<ymin,ymin,ypositions) #Put back particle inside box
        xpositions += numpy.where(this_move == 4, 1, 0)
        xpositions = numpy.where(xpositions>xmax,xmax,xpositions) #Put back particle inside box
        xpositions -= numpy.where(this_move == 3, 1, 0)        
        xpositions = numpy.where(xpositions<xmin,xmin,xpositions) #Put back particle inside box

    return xpositions, ypositions

# Main program
import numpy, sys
#numpy.random.seed(11)

np = int(sys.argv[1])  # number of particles
ns = int(sys.argv[2])  # number of steps
x, y = random_walk_2D(np, ns, -1,1,-1,1)
#print(x,y)
