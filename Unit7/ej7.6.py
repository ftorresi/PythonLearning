class Line:
    """Given 2 points in 2D return the line that joins them"""
    
    def __init__(self,p,q):
        self.m=(p[1]-q[1])/(p[0]-q[0])
        self.h=p[1]-self.m*p[0]
    
    def value(self,x):
        return self.m*x+self.h


def test_Line():
    l=Line((0,1),(1,3))  #y=2x+1
    tol=1e-12
    for x in range(20): #test on 20 points
        x=0.7*x
        y_exp=2*x+1
        y=l.value(x)
        success=abs((y-y_exp))<tol
        assert success, "Bug in Line.value"
        
#line = Line((0,-1), (2,4))
#print (line.value(0.5), line.value(0), line.value(1))
test_Line()
