g=9.8
v0=9.8
n=11
tf=2*v0/g
h=tf/n
t=[h*i for i in range(n+1)]
y=[v0*time-0.5*g*time**2 for time in t] 

print "  t      y"
for a1, a2 in zip(t,y):
 print "%.3f  %.3f"  %(a1,a2)


