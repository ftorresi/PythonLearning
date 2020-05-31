from math import pi, sin, cos, sqrt

lin=lambda x, m=2, h=1: m*x+h  #linear function to test trapezoidal rule

def trapezint(f, a, b, n):
  h=float(b-a)/n
  integral=0.5*h*(f(a)+f(b))
  for i in range(1,n):
    integral+=h*f(a+i*h)
  return integral

def adaptive_trapezint(f, a, b, eps=1E-5):
  dx=0.01 #evaluate f'' on steps of length dx
  x=a  
  h=1e-4 # small number to evaluate derivatives
  d2fmax= abs((f(x-h) - 2*f(x) + f(x+h))/float(h*h))
  while x<=b: #evaluate 2nd derivative of f in many points, to find max of absolute value
    x+=dx 
    d2f=abs((f(x-h) - 2*f(x) + f(x+h))/float(h*h))
    d2fmax=(d2f if d2f > d2fmax else d2fmax) #to keep only the highest value
  c=sqrt(12.0*eps/((b-a)*d2fmax)) #trapezoid separation to get desired error eps
  n=int((b-a)/c)+1 #minimum number of trapezoids
  return n, trapezint(f, a, b, n)

n1,t1= adaptive_trapezint(cos, 0,pi)
n2,t2= adaptive_trapezint(sin, 0,pi)
n3,t3= adaptive_trapezint(sin, 0,0.5*pi)
n4,t4= adaptive_trapezint(sqrt, 4,9)

print "test1 gives %.6f error %.6f for n=%g" %(t1,abs(t1), n1) #exact value =0
print "test2 gives %.6f error %.6f for n=%g" %(t2,abs(t2-2), n2) #exact value =2
print "test3 gives %.6f error %.6f for n=%g" %(t3,abs(t3-1), n3) #exact value =1
print "test4 gives %.6f error %.6f for n=%g" %(t4,abs(t4-38.0/3), n4) #exact value =38/3
   






