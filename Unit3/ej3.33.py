from math import floor #to use in test

#dat=[(0,-1),(1,0),(2,4),(3,6)] 

def ind(x,L=0,R=1):
    return (1 if L<=x<R else 0)

def piecewise2(x, data):
    val=0.0
    for i in range(len(data)-1):
        val+=data[i][1]*ind(x,data[i][0],data[i+1][0])
        #print val
    if x>=data[-1][0]:
        val+=data[-1][1] #last interval must be done separately
    return val

#for i in range(-20,50):
  #x=0.1*i  
  #print "x=",x, piecewise2(x, dat)
  
def test_piecewise2():
    """Test using the piecewise2 floor function, in (0,5)"""
    dat=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
    for i in range(0,555):
        x=0.01*i
        value=piecewise2(x, dat)
        expect=floor(x)
        success=abs(value-expect)<1e-14
        msg="test fails for x=%.2f in floor function" %x
        assert success, msg
        
test_piecewise2()
