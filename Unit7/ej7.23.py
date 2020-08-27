from Polynomials import Polynomial
from math import factorial, exp
import sys

try:
    x=float(sys.argv[1])
    m=[int(sys.argv[2])]
    for num in sys.argv[3:]:
        m.append(int(num))
except:
    print("x and (one or several) N (integers) must be provided")
    sys.exit(1)

n=sorted(m) #sort degrees
#generate coefficients up to nmax
coeffs=[1/factorial(k) for k in range(n[-1]+1)]

poly=[None]*len(n)
for i in range(len(n)):
    poly[i]=Polynomial(coeffs[0:n[i]+1])
    
    
print("Taylor approximation of n-th order:")
for i in range(len(n)):
    print("N=%g,   %g" %(n[i],poly[i](x)))
print("exact value e^x=%g" %exp(x))
