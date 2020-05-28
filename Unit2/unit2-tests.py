#print '------------------'     # table heading
#C = -20                        # start value for C
#dC = 5                         # increment of C in loop
#while C <= 40:                 # loop heading with condition
    #F = (9.0/5)*C + 32         # 1st statement inside loop
    #print C, F                 # 2nd statement inside loop
    #C = C + dC                 # 3rd statement inside loop
#print '------------------'     # end of table line (after loop)


#x = 1.2 # assign some value
#N = 25
## maximum power in sum
#k = 1
#s = x
#sign = 1.0
#import math
#while k < N:
  #sign = - sign
  #k = k + 2
  #term = sign*x**k/math.factorial(k)
  #s = s + term
#print "sin(%g) = %g (approximation with %d terms)" % (x, s, N)


#C = []
#C_value = -50
#C_max = 200
#while C_value <= C_max:
  #C.append(C_value)
  #C_value += 2.5
#print C

#Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
#for C in Cdegrees:
# F = (9.0/5)*C + 32
# print "%5d %5.1f"   %(C, F)

Cdegrees = []
n = 21
C_min = -10
C_max = 40
dC = (C_max - C_min)/float(n-1)
for i in range(0, n):
 C = -10 + i*dC
 Cdegrees.append(C) # increment in C

Fdegrees = []
for C in Cdegrees:
 F = (9.0/5)*C + 32
 Fdegrees.append(F)

for C in Cdegrees:
# C = Cdegrees[i]
 F = Fdegrees[Cdegrees.index(C)]
 print "%5.1f %5.1f" % (C, F)




