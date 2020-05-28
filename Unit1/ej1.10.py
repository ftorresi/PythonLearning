from math import pi, exp, sqrt
m = 0.0
s = 2.0
x = 1.0
f=1/(sqrt(2*pi)*s)*exp(-0.5*((x-m)/s)**2)

print "The value is %.5f" % f
