"""
Same as ej4.21 but parsing arguments from command line.
Example:
--T 2*pi  --n 10,20,30  --alpha 0.1,0.2,0.8 
T must be positive, n must be a list of integers separated by comma (no spaces), alpha must be a list of numbers 0<alpha<1 separated by comma (no spaces)
"""

from math import pi
from sinesum2 import table
import argparse
parser = argparse.ArgumentParser()

def evalcmlarg(text):
    return eval(text)

parser.add_argument("--T", "--function domain max. value", type=evalcmlarg, default=1.0, help="function domain max. value",
metavar="T")

parser.add_argument("--alpha", "--points to evaluate: alpha*T", type=evalcmlarg, default=[0.1,0.2], help="--points to evaluate: alpha*T, 0<alpha<1",metavar="alpha")

parser.add_argument("--n", "--nums. of iterations", type=evalcmlarg, default=[50,100], help="--nums. of iteration",metavar="n")

args = parser.parse_args()

T=args.T; n=args.n; alpha=args.alpha
#print T, alpha, n
table(n, alpha, T)
