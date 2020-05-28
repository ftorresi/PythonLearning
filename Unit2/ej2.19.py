from math import sqrt
for n in range(1, 60):
  r = 2.0
  for i in range(n):
    r = sqrt(r)
  for i in range(n):
    r = r**2
  print "%d times sqrt and **2: %.16f" % (n, r)


n2=52  #smallest n returning 1
r = 2.0
for i in range(n2):
  r = sqrt(r)
  print "%d times sqrt: %.16f" % (i+1, r)
for i in range(n2):
  r = r**2
  print "%d times sqrt and %d times **2: %.16f" % (n2, i+1, r)
