from math import pi, sin, cos

lin=lambda x, m=2, h=1: m*x+h  #linear function to test trapezoidal rule

def trapezint1(f,a,b):
  return 0.5*(b-a)*(f(a)+f(b))

# print trapezint1(lin, 0,1), "linear test, exact=2"
  
### Part b ###

t1= trapezint1(cos, 0,pi)
t2= trapezint1(sin, 0,pi)
t3= trapezint1(sin, 0,0.5*pi)

print "One trapezoid"
print "test1 gives %.4f error %.4f" %(t1,abs(t1)) #exact value =0
print "test2 gives %.4f error %.4f" %(t2,abs(t2-2)) #exact value =2
print "test3 gives %.4f error %.4f" %(t3,abs(t3-1)) #exact value =1

### Part c ###

def trapezint2(f,a,b):
  return 0.25*(b-a)*(f(a)+2*f(0.5*(a+b))+f(b))

t1= trapezint2(cos, 0,pi)
t2= trapezint2(sin, 0,pi)
t3= trapezint2(sin, 0,0.5*pi)

print "Two trapezoids"
print "test1 gives %.4f error %.4f" %(t1,abs(t1)) #exact value =0
print "test2 gives %.4f error %.4f" %(t2,abs(t2-2)) #exact value =2
print "test3 gives %.4f error %.4f" %(t3,abs(t3-1)) #exact value =1

### Part d ###

def trapezint(f, a, b, n):
  h=float(b-a)/n
  integral=0.5*h*(f(a)+f(b))
  for i in range(1,n):
    integral+=h*f(a+i*h)
  return integral

t1= trapezint(cos, 0,pi,10)
t2= trapezint(sin, 0,pi,10)
t3= trapezint(sin, 0,0.5*pi,10)

print "n=10 trapezoids"
print "test1 gives %.4f error %.4f" %(t1,abs(t1)) #exact value =0
print "test2 gives %.4f error %.4f" %(t2,abs(t2-2)) #exact value =2
print "test3 gives %.4f error %.4f" %(t3,abs(t3-1)) #exact value =1


def test_trapezint():
  """test trapezoidal rule which is exact for integral cos x dx from zero to 2*pi, up to 199 trapezoids. """
  for n in range(2,200): #warning! The result isn't correct for n=1
   msg="Test fails for n=%g" %n
   assert (trapezint(cos, 0, 2*pi, n) < 1e-14), msg #exact value=0

test_trapezint()




