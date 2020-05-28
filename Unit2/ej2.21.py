a = 1/947.0*947
b = 1
#if a != b:
# print "Wrong result!, %.16f" %a

tol=1e-12
if abs(a-b) >= tol:
 print "Wrong result!, %.16f" %abs(a-b) 
