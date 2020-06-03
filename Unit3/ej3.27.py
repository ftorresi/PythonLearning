from math import pi, cos


def maxmin(f, a, b, n=1000):
  h=float(b-a)/(n-1) #evaluate f on steps of length h
  x=a  
  fmax=f(x)
  fmin=f(x)
  while x<=b: #evaluate f in many points, to find max and min
    x+=h
    fval=f(x)
    fmax=(fval if fval > fmax else fmax) #to keep only the highest value
    fmin=(fval if fval < fmin else fmin) #to keep only the lowest value
  return fmax, fmin

def test_maxmin():
    """Test maxmin function for cosine"""
    maxexp=1.0
    minexp=-1.0
    maxv,minv=maxmin(cos,-0.5*pi, 2*pi, 1e6)
    succmax=abs(maxexp-maxv)<1e-10
    succmin=abs(minexp-minv)<1e-10
    msgmax= "Test fails for max. in cosine"
    msgmin= "Test fails for min. in cosine"
    assert succmax, msgmax
    assert succmin, msgmin

test_maxmin()






