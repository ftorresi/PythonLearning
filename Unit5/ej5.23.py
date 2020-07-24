""" Making ej5.23 a module
This file is the same as ej5.23 but with a different name so as to be able to export functions (apparently dots not allowed in 'import') """

import numpy as np
import sys
_filename = sys.argv[0]
_usage = """
Tests for errors in the Midpoint rule application: midpointint1 sums in a loop, midpointint2 sums using lists and midpointint3 uses np.sum and arrays.
%s test check for error in those 3 implementations
""" % _filename



def lin(x):
    return 2*x #linear function to test rule

#sum in a loop
def midpointint1(f, a, b, n): 
  h=float(b-a)/n
  integral=0.0
  for i in range(n):
    integral+=h*f(a+(i+0.5)*h)
  return integral

#sum function using lists
def midpointint2(f, a, b, n):
    h=float(b-a)/n
    y=[h*f(a+(i+0.5)*h) for i in range(n)]
    integral=sum(y)
    return integral

#np.sum using arrays
def midpointint3(f, a, b, n):
    h=float(b-a)/n
    x=np.linspace(a+0.5*h,b-0.5*h,n)
    y=h*f(x)
    integral=np.sum(y)
    return integral

def test_midpointint():
  """test mid point rule which is exact for integral cos x dx from zero to 2*pi, up to 199 rectangles. """
  for n in range(2,200): #warning! The result isn't correct for n=1
   msg1="midpoint1 fails for n=%g" %n
   msg2="midpoint2 fails for n=%g" %n
   msg3="midpoint3 fails for n=%g" %n
   assert (abs(midpointint1(lin, 2, 4, n)-12) < 1e-10), msg1
   assert (abs(midpointint2(lin, 2, 4, n)-12) < 1e-10), msg2
   assert (abs(midpointint3(lin, 2, 4, n)-12) < 1e-10), msg3   #exact value=12

if __name__ == "__main__":
    if (len(sys.argv) < 2)or(sys.argv[1]!="test"):
        print (_usage)
    else:
        test_midpointint()
        

#Some ipython time results for (x**2-3*x+1, 0,10,400): 

# midpoint1: 1000 loops, best of 3: 225 µs per loop
# midpoint2: 1000 loops, best of 3: 230 µs per loop
# midpoint3: 10000 loops, best of 3: 50.4 µs per loop
#The implementation 3, using arrays, seems to be 4.5 times faster.




