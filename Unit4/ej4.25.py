from math import factorial as fact
from math import exp
import sys

def poisson(x,t,nu):
    poi=((nu*t)**x)*exp(-nu*t)/fact(x)
    return poi

x=int(sys.argv[1])
t=eval(sys.argv[2])
nu=eval(sys.argv[3])

print poisson(x,t,nu)
