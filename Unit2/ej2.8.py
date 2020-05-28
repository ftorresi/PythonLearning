g=9.8
v0=9.8
n=11
tf=2*v0/g
h=tf/n

print "  t      y"
for i in range(1+n):
  t=h*i
  y=v0*t-0.5*g*t**2
  print "%.3f  %.3f"  %(t,y)

print "---------------"
t=0.0
while t <= (tf+0.01*h):
  y=v0*t-0.5*g*t**2
  print "%.3f  %.3f"  %(t,y)
  t+=h


