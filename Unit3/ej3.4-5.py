def C(f):
    return (5.0/9)*(f-32)

def F(c):
    return 1.8*c+32

if F(C(0))==0 and C(F(5))==5:
    print "functions work OK, naive test"

functions=[F,C]

def test_F_C():
  expect=[0]*2
  for var in range(-50,50,3):
    expect[0]=1.8*var+32
    expect[1]=(5.0/9)*(var-32)
    for i in range(2):
      success=(functions[i](var)-expect[i])<1e-14
#      if ff(cc(var)) != var:  #one of both functions failed
      msg= "%s failed" % functions[i].__name__
      assert success, msg  

test_F_C()

#print F(C(0))
#print C(F(0))
#print F(C(5))
#print C(F(5))


