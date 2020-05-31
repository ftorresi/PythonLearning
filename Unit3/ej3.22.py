from math import pi, exp, sqrt

def gauss(x, m=0, s=1):
    return exp(-0.5*((x-m)/float(s))**2)/(s*sqrt(2*pi))

print "   x      gauss(x)"

n=40
m=0
s=1
h=10.0*s/n
for i in range(n+1):
   x=m-5*s+h*i
   print "%7.3f   %8.5f" %(x,gauss(x, m, s))
