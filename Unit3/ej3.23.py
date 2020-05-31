from math import pi, log

def egg(M, T0=20, Ty=70):
    """Time to take an egg of mass M, at initial temperature T0 to final temperature Ty"""
    #Temperature in Celsius, mass in g.
    rho = 1.038 #egg density
    K = 5.4e-3  #thermal conductivity
    c = 3.7  #specific heat
    Tw=100.0 #boiling water temp.
    time=M**(2./3)*c*rho**(1./3)/(K*pi**2*(4*pi/3.)**(2./3.))*log(0.76*(T0-Tw)/(Ty-Tw)) #time needed
    return time


print """Time (in seconds) needed for soft boiled egg,
in terms of size and initial temperature"""

print "        T0 = 4C  T0 = 25C"
print "M=47g   %6.2f   %6.2f" %(egg(47, 4, 63),egg(47, 25, 63))
print "M=67g   %6.2f   %6.2f" %(egg(67, 4, 63),egg(67, 25, 63))

print """Time (in seconds) needed for hard boiled egg,
in terms of size and initial temperature"""

print "        T0 = 4C  T0 = 25C"
print "M=47g   %6.2f   %6.2f" %(egg(47, 4, 70),egg(47, 25, 70))
print "M=67g   %6.2f   %6.2f" %(egg(67, 4, 70),egg(67, 25, 70))
