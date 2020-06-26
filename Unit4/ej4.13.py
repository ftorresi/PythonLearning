import sys
g = 9.81

try: 
    v0=float(sys.argv[1])
except IndexError:
    print "Initial velocity must be provided"
    v0=float(raw_input("v0=?"))

try: 
    t=float(sys.argv[2])
except IndexError:
    print "Evaluation time must be provided"
    t=float(raw_input("t=?"))

if t < 0:
    raise ValueError("time must be non-negative")
elif t > (2*v0/g):
    raise ValueError("time must be smaller than %.2f" %(2*v0/g) )

y = v0*t - 0.5*g*t**2
print y
