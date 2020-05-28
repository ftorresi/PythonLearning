from math import pi, log
#everything in S.I. units
m = 67.0   #egg mass in g
K = 5.4e-3  #thermal conductivity
c = 3.7  #specific heat
rho = 1.038 #egg density 

T0=4.0 #egg initial temp.
Tw=100.0 #boiling water temp.
Ty=70.0 #egg target temp.

t=m**(2./3)*c*rho**(1./3)/(K*pi**2*(4*pi/3.)**(2./3.))*log(0.76*(T0-Tw)/(Ty-Tw)) #time needed
 
print """ For a large egg (m=%g g)
from the fridge (initial T=%g degrees C)
the ideal time is %.3f s.""" %(m,T0,t)

T0=20.0 #egg initial temp.
t=m**(2./3)*c*rho**(1./3)/(K*pi**2*(4*pi/3.)**(2./3.))*log(0.76*(T0-Tw)/(Ty-Tw)) #time needed

print """ For a large egg (m=%g g)
from room temperature (initial T=%g degrees C)
the ideal time is %.3f s.""" %(m,T0,t)

m=47.0
t=m**(2./3)*c*rho**(1./3)/(K*pi**2*(4*pi/3.)**(2./3.))*log(0.76*(T0-Tw)/(Ty-Tw)) #time needed

print """ For a small egg (m=%g g)
from room temperature (initial T=%g degrees C)
the ideal time is %.3f s.""" %(m,T0,t)



