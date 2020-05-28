from math import pi, sin, exp

def g(t): 
  return exp(-t)*sin(pi*t)

for i in range(11):
  j=0.1*i
  print j,   g(j)



