from math import pi, sin, cos

lin=lambda x, m=2, h=1: m*x+h  #linear function to test rule


def midpointint(f, a, b, n):
  h=float(b-a)/n
  integral=0.0
  for i in range(n):
    integral+=h*f(a+(i+0.5)*h)
  return integral

t1= midpointint(cos, 0,pi,10)
t2= midpointint(sin, 0,pi,10)
t3= midpointint(sin, 0,0.5*pi,10)
#print midpointint(lin,0,1,1)

print "n=10 rectangles"
print "test1 gives %.4f error %.4f" %(t1,abs(t1)) #exact value =0
print "test2 gives %.4f error %.4f" %(t2,abs(t2-2)) #exact value =2
print "test3 gives %.4f error %.4f" %(t3,abs(t3-1)) #exact value =1


def test_midpointint():
  """test mid point rule which is exact for integral cos x dx from zero to 2*pi, up to 199 rectangles. """
  for n in range(2,200): #warning! The result isn't correct for n=1
   msg="Test fails for n=%g" %n
   assert (abs(midpointint(cos, 0, 2*pi, n)) < 1e-14), msg #exact value=0

test_midpointint()




