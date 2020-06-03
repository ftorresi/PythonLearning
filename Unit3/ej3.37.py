from math import cos, pi

def C(x, n=10): 
  x = float(x)
  term = 1.0 #1st term
  s = term
  for i in range(1,n+1):
    term =-term*x**2/(2*i*(2*i-1))
    s += term
  return s

def table(xlist, nlist=[5,25,50,100,200]): 
    """Makes a table evaluating C for values in xlist for ns in nlist"""
    if len(nlist)!=5:
        return "nlist must have 5 real elements"
    for i in range(5):
        if type(nlist[i])!=int:
            return "nlist must have 5 real elements"
    print "   x  %8g  %8g  %8g  %8g  %8g" %(nlist[0],nlist[1],nlist[2],nlist[3],nlist[4])
    error=[0.0]*5
    for x in xlist:
        expect=cos(x)
        for i in range(5):
            error[i]=abs(C(x, nlist[i])-expect)
        print "%7.4f  %8.2e  %8.2e  %8.2e  %8.2e  %8.2e" %(x, error[0],error[1],error[2],error[3],error[4])

        
table([0,0.5*pi, 0.75*pi,2*pi, 4*pi, 6*pi, 8*pi, 10*pi])


