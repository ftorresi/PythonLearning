from math import pi, exp, sqrt
#everything in S.I. units
m = 0.43   #ball mass
g = 9.8  #gravity acceleration
C = 0.4  #drag coefficient
rho = 1.2 #air density 
a = 0.11 #ball radius

area=pi*a**2 #ball cross section 
Fg=m*g  #gravitational force

v=120/3.6 #ball speed in a hard kick
Fd=0.5*C*rho*area*v**2 #drag force
ratio=Fd/Fg

print """ For a hard kick (v=%.3f m/s),
the drag force is %.3f N
and the gravitational force is %.3f N. 
The ratio drag/grav is %.3f""" %(v,Fd,Fg,ratio)



v=30/3.6 #ball speed in a hard kick
Fd=0.5*C*rho*area*v**2 #drag force
ratio=Fd/Fg

print """ For a soft kick (v=%.3f m/s),
the drag force is %.3f N
and the gravitational force is %.3f N. 
The ratio drag/grav is %.3f""" %(v,Fd,Fg,ratio)
