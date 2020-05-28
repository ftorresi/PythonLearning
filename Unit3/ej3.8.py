from math import sqrt

# item a)

def roots(a,b,c):
   """gives solutions of ax**2+bx+c=0 for a,b,c reals"""
   if not ((type(a)==float or type(a)==int) and (type(b)==float or type(b)==int) and (type(c)==float or type(c)==int)):
    print "Coefficients must be real!"
    return None, None
   elif abs(a) < 1e-14:
    print "Cuadratic coefficient must be non-zero!"
    return None, None
   else: 
    det=b**2-4*a*c
    if abs(det) < 1e-14:
     x1=-b/(2.0*a)
     x2=x1
    elif det > 1e-14:
     x1=(-b-sqrt(det))/(2.0*a)
     x2=(-b+sqrt(det))/(2.0*a)
    else:
     xr=-b/(2.0*a)
     xi=(-sqrt(-det))/(2.0*a)
     x1=xr+xi*1j
     x2=xr-xi*1j
   return x1, x2

#r1, r2 =  roots(1,-2,2)
#print r1, r2

#item b)
def test_root_float():
  """ test function for roots with float solutions"""
  a2=1
  a1=1.5
  a0=-2.5 #solutions are 1 and -2.5
  exact1=-2.5
  exact2=1
  r1, r2 = roots(a2,a1,a0)
  success=(abs(r1-exact1)<1e-14 and abs(r2-exact2)<1e-14)
  msg= "root fails for float solutions!"
  assert success, msg


def test_root_cmplx():
  """ test function for roots with complex solutions"""
  a2=1
  a1=-2
  a0=2. #solutions are 1+j and 1-j
  exact1=1-1j
  exact2=1+1j
  r1, r2 = roots(a2,a1,a0)
  success=(abs(r1-exact1)<1e-14 and abs(r2-exact2)<1e-14)
  msg= "root fails for cmplx solutions!"
  assert success, msg
  
test_root_float()
test_root_cmplx()






