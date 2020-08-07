

def triangle_area(vertices):
    area=0.5*abs(vertices[1][0]*vertices[2][1]-vertices[2][0]*vertices[1][1]-vertices[3][0]*vertices[2][1]+vertices[2][0]*vertices[3][1]+vertices[3][0]*vertices[1][1]-vertices[1][0]*vertices[3][1])
    return area


#vert={1:(0,0),2:(1,0),3:(1,1)}
#print (triangle_area(vert))

    
def test_triangle_area():
   """
   Verify the area of a triangle with vertex coordinates
   (0,0), (1,0), and (0,2).
   """
   v1 = (0,0); v2 = (1,0); v3 = (0,2)
   vertices = {1:v1, 2:v2, 3:v3}
   expected = 1
   computed = triangle_area(vertices)
   tol = 1E-14
   success = abs(expected - computed) < tol
   msg = "computed area=%g != %g (expected)" % \
         (computed, expected)
   assert success, msg
   
test_triangle_area()
