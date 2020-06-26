def midpoint_integration(f, a, b, n=100):
    h = (b - a)/float(n)
    I = 0
    for i in range(n):
        I += f(a + i*h + 0.5*h)
    return h*I

from math import *
import sys
from scitools.StringFunction import StringFunction
f_formula = sys.argv[1]
a = eval(sys.argv[2])
b = eval(sys.argv[3])
if len(sys.argv) >= 5:
    n = int(sys.argv[4])
else:
    n = 200

g=StringFunction(f_formula)

I = midpoint_integration(g, a, b, n)
print 'Integral of %s on [%g, %g] with n=%d: %g' % \
      (f_formula, a, b, n, I)

def test_midpoint():
    ov1=midpoint_integration(cos, 0, 2*pi) #expected=0
    ov2=midpoint_integration(sin, 0, pi, n=1000) #expected=2
    success=(abs(ov1)<1e-6)and(abs(ov2-2)<1e-6)
    msg="test failed"
    assert success, msg


#test_midpoint()
