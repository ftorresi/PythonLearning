def polygon_area(x, y):
    if len(x)!=len(y):
        print "both argumets must have the same number of elements!"
        return
    else:
      area=0.0
      for i in range(len(x)-1): # i=0 to len(x)-2; last term must be done separately
          area+=x[i]*y[i+1]-x[i+1]*y[i]
      area+=x[len(x)-1]*y[0]-x[0]*y[len(x)-1] #connect last and fist vertices
      area=0.5*abs(area)    
      return area

### Test for triangle

xtest=[0, 2, 0,]
ytest=[0, 0, 1,]

print "Triangle test area=%g, exact=1" %polygon_area(xtest, ytest)

### Test for cuadrilateral

xtest=[0, 2, 12, 10]
ytest=[0, 2, 2, 0]

print "Cuadrilateral test area=%g, exact=20" %polygon_area(xtest, ytest)

### Test for pentagon

xtest=[0, 2, 3, 2, 0]
ytest=[0, 0, 1, 2, 2]

print "Pentagon test area=%g, exact=5" %polygon_area(xtest, ytest)
