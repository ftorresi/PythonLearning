from math import sin

class Root:
    def __init__(self,f,dfdx=None):
        self.f=f
        if dfdx is None: 
            def dfdx(x):
                h=1E-5
                return (f(x+h)-f(x-h))/(2*h)
        self.dfdx=dfdx
        
    def solve(self,start_values=[0], max_iter=100, tolerance=1E-6):
        self.x=start_values #Hold approximations
        self.fv=[]
        for xx in self.x: #build list of f(x)
            self.fv.append(self.f(xx))
        i=0
        delta=tolerance+1
        while (i<max_iter and delta>tolerance):
            self.method() #call method
            i+=1 #increase counter
            delta=abs(self.fv[-1]-self.fv[-2]) #calculate error approx.
        b=bool(delta<tolerance)
        return self.x[-1],self.fv[-1],self.x,self.fv,i,b
            
    
class Bisection(Root):
    def method(self):
        #Note that the book suggestion, self.x[-3:], not neccessarily will include the correct numbers
        #Ej, for root=0.99, starting interval [0,1], we have self.x=[0,1,0.5,0.75,0.875] and then the function has the same sign for the last 3 values of self.x
        #hence the need for our j-loop over self.x
        try:
            for j in range(len(self.fv)):
                if self.fv[-1]*self.fv[-2-j]<=0: #interval has a root
                    r=0.5*(self.x[-1]+self.x[-2-j])
                    break #stop j-loop
        except:
            print("No root in the specified interval")
        self.x.append(r),self.fv.append(self.f(r)) #add new values to lists
        
        
class Newton(Root):
    def method(self):
        try:
            r=self.x[-1]-self.fv[-1]/self.dfdx(self.x[-1])
        except:
            print("Error: df/dx=0 found") 
        self.x.append(r),self.fv.append(self.f(r)) #add new values to lists
        
class Secant(Root):
    def method(self): #no need to raise exception since if denominator==0, method had converged
        r=self.x[-1]-self.fv[-1]*(self.x[-1]-self.x[-2])/(self.fv[-1]-self.fv[-2])
        self.x.append(r),self.fv.append(self.f(r)) #add new values to lists
    
    
def test_Root():
    def g(x):
        #return 2*x-3
        return x**2-x-1 #one root approx. 1.61803399, the other one is negative
        #return x**5-sin(x) #change sign in [0.1,1]
    
    exact=(1+5**0.5)/2
    gbis=Bisection(g)
    root,val,rlist,vlist,iter_num,tol_cond=gbis.solve([0,2],tolerance=1E-8)
    assert abs(root-exact)<1e-8, "Bug in Bisection"
    #print("root %g, val %g found in %g iterations using BISECTION"%(root,val,iter_num))
    #print("tolerance condition met?",tol_cond)
    #print("list of intermediate values")
    #print("x, g(x)")
    #for i in range(len(rlist)):
        #print("%g %g"%(rlist[i],vlist[i]))
        
        
    gnewton=Newton(g)
    root,val,rlist,vlist,iter_num,tol_cond=gnewton.solve([1],tolerance=1E-8)
    assert abs(root-exact)<1e-10, "Bug in Newton"
    #print("root %g, val %g found in %g iterations using NEWTON"%(root,val,iter_num))
    #print("tolerance condition met?",tol_cond)
    #print("list of intermediate values")
    #print("x, g(x)")
    #for i in range(len(rlist)):
        #print("%g %g"%(rlist[i],vlist[i]))
        
    gsec=Secant(g)
    root,val,rlist,vlist,iter_num,tol_cond=gsec.solve([1,13],tolerance=1E-8)
    assert abs(root-exact)<1e-10, "Bug in Secant"
    #print("root %g, val %g found in %g iterations using SECANT"%(root,val,iter_num))
    #print("tolerance condition met?",tol_cond)
    #print("list of intermediate values")
    #print("x, g(x)")
    #for i in range(len(rlist)):
        #print("%g %g"%(rlist[i],vlist[i]))
        
        
        
        
if __name__ == '__main__':
    test_Root()
