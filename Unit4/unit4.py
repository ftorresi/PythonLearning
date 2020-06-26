#C = raw_input("C=? ")
#C = float(C)
#F = 9.0/5*C + 32
#print F

#import sys
#C = float(sys.argv[1])
#F = 9.0*C/5 + 32
#print F

#import sys
#t = float(sys.argv[1])
#v0 = float(sys.argv[2])
#g = 9.81
#y = v0*t - 0.5*g*t**2
#print y

#import sys
#s = 0
#for arg in sys.argv[1:]:
  #number = float(arg)
  #s += number
#print "The sum of ",
#for arg in sys.argv[1:]:
  #print arg,
#print "is ", s

#import sys
#s = sum([float(x) for x in sys.argv[1:]])
#print "The sum of %s is %s" % (" ".join(sys.argv[1:]), s)


## Set default values
#s0 = v0 = 0; a = t = 1
#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument('--v0', '--initial_velocity', type=float,
                    #default=0.0, help='initial velocity',
                    #metavar='v')
#parser.add_argument('--s0', '--initial_position', type=float,
                    #default=0.0, help='initial position',
                    #metavar='s')
#parser.add_argument('--a', '--acceleration', type=float,
                    #default=1.0, help='acceleration', metavar='a')
#parser.add_argument('--t', '--time', type=float,
                    #default=1.0, help='time', metavar='t')

#args = parser.parse_args()
#s0 = args.s0; v0 = args.v0; a = args.a; t = args.t
#s = s0 + v0*t + 0.5*a*t**2
#print """
#An object, starting at s=%g at t=0 with initial
#velocity %s m/s, and subject to a constant
#acceleration %g m/s**2, is found at the
#location s=%g m after %s seconds.
#""" % (s0, v0, a, s, t)



"""
As location.py, but using our own function for interpreting each
string from the command-line via eval.
"""
# Set default values
s0 = v0 = 0; a = t = 1

#from math import *

#def evalcmlarg(text):
    #return eval(text)

#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument('--v0', '--initial_velocity', type=evalcmlarg, default=0.0, help='initial velocity')
#parser.add_argument('--s0', '--initial_position', type=evalcmlarg, default=0.0, help='initial position')
#parser.add_argument('--a', '--acceleration', type=evalcmlarg, default=1.0, help='acceleration')
#parser.add_argument('--t', '--time', type=evalcmlarg, default=1.0, help='time')

#example = "--s0 'exp(-4.2)' --v0 pi/4"
##args = parser.parse_args(example.split())
#args = parser.parse_args()
#s0 = args.s0; v0 = args.v0; a = args.a; t = args.t
#s = s0 + v0*t + 0.5*a*t**2
#print """
#An object, starting at s=%g at t=0 with initial
#velocity %s m/s, and subject to a constant
#acceleration %g m/s**2, is found at the
#location s=%g m after %s seconds.
#""" % (s0, v0, a, s, t)


import sys

def read_C():
    try:
        C = float(sys.argv[1])
    except IndexError:
        raise IndexError\
        ('Celsius degrees must be supplied on the command line')
    except ValueError:
        raise ValueError\
        ('Celsius degrees must be a pure number, '\
         'not "%s"' % sys.argv[1])
    # C is read correctly as a number, but can have wrong value:
    if C < -273.15:
        raise ValueError('C=%g is a non-physical value!' % C)
    return C

try:
    C = read_C()
except (IndexError, ValueError) as e:
    print e
    sys.exit(1)

F = 9.0*C/5 + 32
print '%gC is %.1fF' % (C, F)
