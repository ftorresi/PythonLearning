
root=[1,-1,4,-3]

def poly(x,roots):
    prod=1.0
    for r in roots:
      prod*=(x-r)
    return prod


def test_poly():
    """test for poly, checks roots and value for x=0"""
    trial_roots=[1,-4,9,-3,7,1,6]
    y0=(-1.)**(len(trial_roots))
    success=[]
    obtain=[]
    for i in trial_roots:
       y0*=i
       obtain.append(poly(i,trial_roots))
       success.append(0.0)
    success.append(y0)
    obtain.append(poly(0,trial_roots))
    for j,k in zip(success,obtain)[0:-1]:  #check if roots are ok
      assert (abs(j-k)<1e-14), "One root that should be, is not"
    assert (abs(success[-1]-obtain[-1])<1e-14), "y0 value is not correct"
    
test_poly()    
