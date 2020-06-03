from math import floor #to use in test

#dat=[(0,-1),(1,0),(1.5,4),(2,6)] 

def piecewise(x, data): #data=[(xi,vi)]
    if x<data[0][0]:
        print "argument must be greater than %.2f" %data[0][0]
        return None
    for i in range(len(data)): #first check if x=xi for any i
        if x == data[i][0]:
            val=data[i][1]
            return val
    for i in range(len(data)-1):
        if(x-data[i][0])*(x-data[i+1][0])<0: #this means x belongs to (xi,x(i+1))
            val=data[i][1]
            return val
        elif(x>data[-1][0]):  #last interval must be done separately
            val=data[-1][1]
            return val
        
#for i in range(-20,50):
  #x=0.1*i  
  #print x,piecewise(x, dat)

def test_piecewise():
    """Test using the piecewise floor function, in (0,5)"""
    dat=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
    for i in range(0,555):
        x=0.01*i
        value=piecewise(x, dat)
        expect=floor(x)
        success=abs(value-expect)<1e-14
        msg="test fails for x=%.2f in floor function" %x
        assert success, msg
        
test_piecewise()
