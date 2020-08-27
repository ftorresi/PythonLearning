from Derivative import Derivative
from Y import Y

v0=50
y=Y(v0)
dydt=Derivative(y)

t0=0
dy0=dydt(t0)
dy0exact=v0
print ("For t=%g, v=%g, expected v=%g" %(t0, dy0, dy0exact))

t1=0.5*v0/y.g
dy1=dydt(t1)
dy1exact=0.5*v0
print ("For t=%g, v=%g, expected v=%g" %(t1, dy1, dy1exact))

t2=v0/y.g
dy2=dydt(t2)
dy2exact=0
print ("For t=%g, v=%g, expected v=%g" %(t2, dy2, dy2exact))
