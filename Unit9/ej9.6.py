class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    
class PolarPoint(Point):
    def __init__(self, r, theta=None):
        self.r, self.theta= r, theta
        if (theta==None and r==0): 
            x,y=0,0
        else:
            from math import sin, cos
            x=r*cos(theta)
            y=r*sin(theta)
        Point.__init__(self,x,y)
        
    def __str__(self):
        if self.theta==None:
             return 'Cartesian: (0, 0) \n Polar: r=0'
        else:
            return 'Cartesian: (%g, %g) \n Polar: (%g, %g)' % (self.x, self.y, self.r, self.theta)
        
#from math import pi,sqrt
#p1=Point(3,4)
#p2=PolarPoint(sqrt(2),pi/4)
#print(p1)
#print(p2)

def test_points():
    from math import pi,sqrt
    p1=PolarPoint(sqrt(2),pi/4)
    x1=1; y1=1
    p2=PolarPoint(5,2)
    x2=-2.080734183; y2=4.546487134
    tol=1e-8
    success=abs(x1-p1.x)<tol and abs(y1-p1.y)<tol
    assert success, "Error for p1"
    success=abs(x2-p2.x)<tol and abs(y2-p2.y)<tol
    assert success, "Error for p2"
    
test_points()
