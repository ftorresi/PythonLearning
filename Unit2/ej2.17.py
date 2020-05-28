g=9.8
v0=9.8
n=11
tf=2*v0/g
h=tf/n
t=[h*i for i in range(n+1)]
y=[v0*time-0.5*g*time**2 for time in t] 

print "Part (a)"
ty1=[t,y]

print "  t      y"
for i in range(len(t)):
 print "%.2f  %.2f"  %(ty1[0][i],ty1[1][i])

print "--------------"
print "Part (b)"

ty2=[]
for a,b in zip(t,y):
  ty2.append([a,b])

print "  t      y"
for a,b in ty2:
  print "%.2f  %.2f"  %(a,b)


