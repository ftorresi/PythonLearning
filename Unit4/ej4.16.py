import sys

try: 
    v0=float(sys.argv[1])
except IndexError:
    print "Initial velocity must be provided"
    v0=float(raw_input("v0 in km/h=?"))

try: 
    mu=float(sys.argv[2])
except IndexError:
    print "Evaluation time must be provided"
    mu=float(raw_input("friction coefficient=?"))

v0=v0/3.6
g = 9.81
d = 0.5*v0**2/(mu*g)
print "distance needed: %.2f m" %d
