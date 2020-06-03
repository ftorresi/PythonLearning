def kinematics(x, t):  #I calculate v and a for every i instead of doing it for a given i, i=1,...,len(x)-1
    if (len(x)==len(t)):
      v=[0]*(len(x)-2)
      a=[0]*(len(x)-2)
      for i in range(1,len(x)-1):
          v[i-1]=float(x[i+1]-x[i-1])/(t[i+1]-t[i-1])
          a[i-1]=(2.0/(t[i+1]-t[i-1]))*((float(x[i+1]-x[i])/(t[i+1]-t[i]))-(float(x[i]-x[i-1])/(t[i]-t[i-1])))
      return v, a
    else:
        print "Position and time lists must have the same number of elements"
        return None

#Manual test for constant acceleration

#xtest=[0,1,4,9,16]
#ttest=[0,1,2,3,4]
#vt, at= kinematics(xtest, ttest)
#print vt, at

# Test function

def test_kinematics():
    t0=[0,0.5,1.5,2.2,3]
    x0=[2.5*tau for tau in t0]
    vexpect=[2.5]*3
    aexpect=[0.0]*3
    vval, aval = kinematics(x0, t0)
    esum=0.0
    for i in range(len(vval)):
        esum+=abs(vval[i]-vexpect[i])+abs(aval[i]-aexpect[i])
    success= esum < 2.0*len(vval)*1e-14
    msg="test fails for constant velocity"
    assert success, msg

test_kinematics()
