from math import sqrt

class Rectangle(object):
    
    def __init__(self,x0,y0,width,height):
        self.x0, self.y0, self.width, self.height=x0, y0, width, height
    
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return 2*(self.width+self.height)
    

class Triangle(object):
    
    def __init__(self,x0,y0,x1,y1,x2,y2):
        self.x0, self.y0, self.x1, self.y1, self.x2, self.y2=x0, y0, x1, y1, x2, y2
        
    def area(self):
        x0, y0, x1, y1, x2, y2=self.x0, self.y0, self.x1, self.y1, self.x2, self.y2
        return 0.5*abs(x1*y2-x2*y1-x0*y2+x2*y0+x0*y1-x1*y0) 
    
    def perimeter(self):
        x0, y0, x1, y1, x2, y2=self.x0, self.y0, self.x1, self.y1, self.x2, self.y2
        return sqrt((x1-x0)**2+(y1-y0)**2)+sqrt((x2-x0)**2+(y2-y0)**2)+sqrt((x1-x2)**2+(y1-y2)**2)


def test_Rectangle():
    w = 2.5
    h = 2
    r = Rectangle (7.4, -8.1, w, h)
    expected_area = w*h
    computed_area = r.area()
    diff = abs(expected_area - computed_area)
    tol = 1E-14
    assert diff < tol, "bug in Rectangle.area, diff=%s" %diff
    
    expected_perimeter = 2*(h+w)
    computed_perimeter = r.perimeter()
    diff = abs(expected_perimeter - computed_perimeter)
    assert diff < tol, "bug in Rectangle.perimeter, diff=%s" %diff
    
    
def test_Triangle():
    t = Triangle (0,0,0,3,4,0)
    expected_area = 6
    computed_area = t.area()
    diff = abs(expected_area - computed_area)
    tol = 1E-14
    assert diff < tol, "bug in Triangle.area, diff=%s" %diff
    
    expected_perimeter = 12
    computed_perimeter = t.perimeter()
    diff = abs(expected_perimeter - computed_perimeter)
    assert diff < tol, "bug in Triangle.perimeter, diff=%s" %diff
    
test_Rectangle()
test_Triangle()
