class Line:
    """Given (in 2D) 2 points, a point and a slope, or a slope and the y-intersection,
     return the line is specified by such data"""
    
    def __init__(self,p,q):
        if (isinstance(p, (list,tuple)) and isinstance(q, (list,tuple))): # two points
            self.m=(p[1]-q[1])/(p[0]-q[0])
            self.h=p[1]-self.m*p[0]
        if isinstance(p, (tuple,list)) and isinstance(q, (float,int)): #point and slope
            self.m=q
            self.h=p[1]-self.m*p[0]
        if isinstance(p, (float,int)) and isinstance(q, (tuple,list)): #slope and point
            self.m=p
            self.h=q[1]-self.m*q[0]
        if isinstance(p, (float,int)) and isinstance(q, (float,int)): #slope and y-intersection
            self.m=p
            self.h=q
    
    def value(self,x):
        return self.m*x+self.h


def test_Line():
    l2p=Line((0,1),(1,3))  #y=2x+1
    lps=Line((1,3),2)
    lsp=Line(2,(0,1))
    lsy=Line(2,1)
    tol=1e-12
    for x in range(20): #test on 20 points
        x=0.7*x
        y_exp=2*x+1
        y=l2p.value(x)
        success=abs((y-y_exp))<tol
        assert success, "Bug in Line.value for two points"
        y=lps.value(x)
        success=abs((y-y_exp))<tol
        assert success, "Bug in Line.value for point and slope"
        y=lsp.value(x)
        success=abs((y-y_exp))<tol
        assert success, "Bug in Line.value for slope and point"
        y=lsy.value(x)
        success=abs((y-y_exp))<tol
        assert success, "Bug in Line.value for slope and y-intersection"
        
#line = Line( (2,3),(0,0))
#print(line.m, line.h)
#print (line.value(0.5), line.value(0), line.value(1))
test_Line()
