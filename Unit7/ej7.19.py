from math import sin, pi
import numpy as np

class Heaviside:
    
    def __init__(self,eps=None):
            self.eps=eps
        
    def __call__(self,x):
        eps=self.eps
        r=np.zeros_like(x)
        if eps==None:
            condition=x>=0
            r[condition]=1.0
            
        else:
            x=np.asarray(x)
            condition1=np.logical_and(-eps<=x , x<=eps)
            condition2=x>eps
            
            r[condition1]=0.5+x[condition1]/(2*eps)+np.sin(np.pi*x[condition1]/eps)/(2*np.pi)
            r[condition2]=1.0
        
        return r

    def plot(self,xmin=-1.,xmax=1.):
        eps=self.eps
        if eps==None:
            x=np.array([xmin,-1e-14,1e-14,xmax])
            y=np.array([0,0,1,1])
            if not xmin*xmax<0: #exceptions to the 'optimal' case
                if xmin>=0:
                    x=np.array([xmin,xmax])
                    y=np.array([1,1])
                elif xmax==0:
                    x=np.array([xmin,-1e-14,xmax])
                    y=np.array([0,0,1])
                elif xmax<0:
                    x=np.array([xmin,xmax])
                    y=np.array([0,0])
        
        else:
            start=max(xmin,-eps)
            end=min(xmax,eps)
            x=np.linspace(start,end,201) #make fine grid from -eps to eps, or xmin/xmax if those are greater/smaller
            x=x.tolist() #make list, to add points if neccessary
            if xmin<-eps:
                x.insert(0, xmin) #insert xmin
            if xmax>eps:
                x.insert(-1, xmax) #insert xmax
            x=np.asarray(x) #Make array
            y=self.__call__(x)
            
        return x, y  
    
    
    
def test_Heaviside():
    ep=0.1
    H = Heaviside()   #original H
    assert (H(0.1)-1==0), "bug in original discontinous Heaviside function for x>0"
    assert (H(-0.1)==0), "bug in original discontinous Heaviside function for x<0"
    x = np.array([-0.15,-0.05,0,0.05,0.15])
    exact=np.array([0,0,1,1,1])
    diff=max(abs(H(x)-exact))
    assert diff<1e-14, "bug in original discontinous Heaviside function for arrays"
    
    
    H = Heaviside(ep) # smoothed Heaviside function
    assert (H(ep+0.1)-1==0), "bug in smoothed Heaviside function for x>eps"
    assert (H(-ep-0.1)==0), "bug in smoothed Heaviside function for x<-eps"
    assert (abs(H(0.0)-0.5)<1e-14), "bug in smoothed Heaviside function for x=0"
    assert (0<H(-ep/2)<0.5), "bug in smoothed Heaviside function for 0>x>-eps"
    assert (0.5<H(ep/2)<1), "bug in smoothed Heaviside function for 0<x<-eps"
    
    x = np.array([-0.15,0,0.15])
    exact=np.array([0,0.5,1])
    diff=max(abs(H(x)-exact))
    assert diff<1e-14, "bug in original smoothed Heaviside function for arrays"
    x=np.array([-0.05,0.05])
    test=H(x)>0.5
    test_exact=[False,True]
    assert (test==test_exact).all, "bug in sign of original smoothed Heaviside function for arrays in [-eps,eps] interval"
    
test_Heaviside()   
    
            
#H = Heaviside()   #original H
#print (H(0.1))
#H = Heaviside(eps=0.8) #smoothed H
#print (H(0.1))

#H = Heaviside()  # original discontinous Heaviside function
#x = np.linspace(-1, 1, 11)
#print (H(x))
#H = Heaviside(eps=0.8) # smoothed Heaviside function
#print (H(x))


#H = Heaviside()
#x, y = H.plot(-4,4) # x in [-4, 4]
#from matplotlib.pyplot import plot, show
#plot(x, y)
#H = Heaviside(eps=1)
#x, y = H.plot(xmin=-4, xmax=4)
#plot(x, y)
##show()

