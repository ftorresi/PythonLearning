import numpy as np

class LagrangeInterpolation:
    """Given a set of points, interpolate them via Lagrange method"""
    
    def __init__(self,xp,yp):
        self.xp=xp
        self.yp=yp
        
    
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
        ## Compute some interpolation points along y=sin(x)
        #xp = np.linspace(0, np.pi, 5)
        #yp = np.sin(xp)
        
        ## Lagrange's interpolation polynomial
        #p_L = LagrangeInterpolation(xp, yp)
        #x = 1.2
        #print ('p_L(%g)=%g' % (x, p_L(x)))
        #print ('sin(%g)=%g' % (x, np.sin(x)))
        #p_L.plot()
        ## show graph of p_L
