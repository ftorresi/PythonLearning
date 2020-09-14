import numpy  # not as np since np is an important variable here
import time, sys

try:
    x0 = int(sys.argv[1])  # Initial money
    F = int(sys.argv[2])  # Target Fortune
    p=float(sys.argv[3]) #Winning probability
except IndexError:
    x0= 10
    F = 100 
    p=0.7 #Using p<0.5 takes TOO LONG
    
def number_of_games(x0,F,p):
    ns= 10000000 #batch size
    position = x0 #Only 1 particle starting at x0
    count=0
    
    # Draw from 1, 2
    moves = numpy.random.random_integers(1, 2, size=ns)
    # Transform 1 to -1 and 2 to 1
    moves = 2*moves - 3
    
    while (position!=F):
        count+=1
        # Draw from [0,1)
        moves = numpy.random.rand(ns)
        # Transform 1 to -1 according to p
        moves=numpy.where(moves<p,1,-1)
        for step in range(ns):
            position += moves[step]
            if position==F:
                realstep=(count-1)*ns+step+1
                #print("A fortune of %i euro was reached in %i steps" %(F, realstep))
                return realstep
            

N=int(input("Number of experiments? "))
t0=time.clock()
M=number_of_games(x0,F,p)
t1=time.clock()
texp=t1-t0
print("Time for 1st experiment: %g s"%texp)

for i in range(1,N):
    M+=number_of_games(x0,F,p)
M/=N
print("It took an average of %i games to go from %i to %i euro playing a game with winning probability %g"%(M,x0,F,p))

r=numpy.log(M)/numpy.log(F-x0)
print("The exponent r results %g"%r)
