

def triangle_area(vertices):
    area=0.5*abs(vertices[1][0]*vertices[2][1]-vertices[2][0]*vertices[1][1]-vertices[0][0]*vertices[2][1]+vertices[2][0]*vertices[0][1]+vertices[0][0]*vertices[1][1]-vertices[1][0]*vertices[0][1])
    return area

v1=[0,0]
v2=[1,0]
v3=[0,2]
v4=[2,0]
v5=[-1,-1]
v6=[1,-2]

t1=[v1,v2,v3]
t2=[v1,v3,v2]
t3=[v4,v2,v3]
t4=[v1,v5,v3]
t5=[v1,v2,v6]
t6=[v4,v1,v2]

print triangle_area(t1)
print triangle_area(t2)
print triangle_area(t3)
print triangle_area(t4)
print triangle_area(t5)
print triangle_area(t6) 
    
    
    
def test_triangle_area():
   """
   Verify the area of a triangle with vertex coordinates
   (0,0), (1,0), and (0,2).
   """
   v1 = (0,0); v2 = (1,0); v3 = (0,2)
   vertices = [v1, v2, v3]
   expected = 1
   computed = triangle_area(vertices)
   tol = 1E-14
   success = abs(expected - computed) < tol
   msg = "computed area=%g != %g (expected)" % \
         (computed, expected)
   assert success, msg
   
test_triangle_area()
