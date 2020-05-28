from math import sin, cos, pi
x = pi/4
val1 = sin(x)**2 + cos(x)**2
print val1

v0 = 3 
t = 1 
a = 2 
s = v0*t + 0.5*a*t**2
print "The distance is %.2f m" %s

a = 3.3
b = 5.3
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2
print "First equation: %g = %g" % (eq1_sum, eq1_pow)
print "Second equation: %g = %g" % (eq2_pow, eq2_pow)
