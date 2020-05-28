from math import pi, sin, exp

def h(t,a=10): 
  return exp(-a*t)*sin(pi*t)

for i in range(11):
  j=0.1*i
  print j,   h(j)
