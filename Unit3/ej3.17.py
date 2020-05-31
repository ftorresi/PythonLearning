from math import sqrt
#xtest=[0, 1, 1]
#ytest=[0, 0, 1]

def pathlength(x, y):
    if len(x)!=len(y):
        print "both argumets must have the same number of elements!"
        return
    else:
      leng=0.0
      for i in range(1,len(x)):
          leng+=sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
      return leng

#print pathlength(xtest, ytest)

## part b ##

def test_pathlength():
  """
  Verify the length of a square path with vertex coordinates
  (0,0), (1,0), (1,1), (0,1) and (0,0).
  """    
  x=[0, 1, 1, 0, 0]
  y=[0, 0, 1, 1, 0]
  expected = 4
  computed = pathlength(x, y)
  success = abs(expected - computed) < 1e-14
  msg = "computed lenth=%g != %g (expected)" %(computed, expected)
  assert success, msg

test_pathlength()
