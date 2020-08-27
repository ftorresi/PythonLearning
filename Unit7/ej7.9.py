import numpy as np

class LagrangeInterpolation:
    """Given a set of points, interpolate them via Lagrange method"""
    
    def __init__(self,arg1,arg2,arg3=None):
        if (isinstance(arg1,np.ndarray) and isinstance(arg2,np.ndarray)):  
            self.xp=arg1
            self.yp=arg2
        elif (callable(arg1) and isinstance(arg2,(list,tuple)) and isinstance(arg3,int)):
            self.f=arg1
            self.xmin=arg2[0]
            self.xmax=arg2[1]
            self.n=arg3
            self.xp=np.linspace(self.xmin,self.xmax,self.n)
            self.yp=self.f(self.xp)
                  
                  
    
    def __call__(self,x):
        from Lagrange_poly2b import p_L
        return p_L(x, self.xp, self.yp)
    
    def plot(self):
        from Lagrange_poly2b import graph
        graph(self.xp, self.yp, resolution=1001)

def test_LagrangeInterpolation():
    xq=np.linspace(0,np.pi,5)
    yq=np.sin(xq)
    pL=LagrangeInterpolation(xq, yq)
    pL=LagrangeInterpolation(np.sin,[0,np.pi],5)
    for j in range(xq.size): 
        yout=pL(xq[j])
        assert abs(yout-yq[j])<1e-10, "The polynomial misses some point(s)"
    x0=(xq[1]+xq[2])/2 #trial point in the middle
    y0=np.sin(x0) #exact value
    ylagrange=pL(x0)
    print("No errors. \nExample: for x=%.3f, sin(x)=%.4f and the interpolated value with 5 equally spaced points in [0, pi] gives %.4f" %(x0,y0,ylagrange))


if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        test_LagrangeInterpolation()
        
        ## Lagrange's interpolation for a given function, interval and number of points
        #p_L = LagrangeInterpolation(np.sin,[0,np.pi],5)
        #x = 1.2
        #print ('p_L(%g)=%g' % (x, p_L(x)))
        #print ('sin(%g)=%g' % (x, np.sin(x)))
        #p_L.plot()
        ## show graph of p_L
