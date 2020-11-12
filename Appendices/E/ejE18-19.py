"""ODE for the inverse of a function - as a class"""
"""With copy-paste of classes that shoud be imported in a _real_ situation"""
import numpy as np
import matplotlib.pyplot as plt
class ODESolver:
    """
    Superclass for numerical methods solving scalar and vector ODEs

      du/dt = f(u, t)

    Attributes:
    t: array of time values
    u: array of solution values (at time points t)
    k: step number of the most recently computed solution
    f: callable object implementing f(u, t)
    """
    def __init__(self, f):
        if not callable(f):
            raise TypeError('f is %s, not a function' % type(f))
        # For ODE systems, f will often return a list, but
        # arithmetic operations with f in numerical methods
        # require that f is an array. Let self.f be a function
        # that first calls f(u,t) and then ensures that the
        # result is an array of floats.
        self.f = lambda u, t: np.asarray(f(u, t), float)

    def advance(self):
        """Advance solution one time step."""
        raise NotImplementedError

    def set_initial_condition(self, U0):
        if isinstance(U0, (float,int)):  # scalar ODE
            self.neq = 1
            U0 = float(U0)
        else:                            # system of ODEs
            U0 = np.asarray(U0)          # (assume U0 is sequence)
            self.neq = U0.size
        self.U0 = U0

        # Check that f returns correct length:
        try:
            f0 = self.f(self.U0, 0)
        except IndexError:
            raise IndexError('Index of u out of bounds in f(u,t) func. Legal indices are %s' % (str(range(self.neq))))
        if f0.size != self.neq:
            raise ValueError('f(u,t) returns %d components, while u has %d components' % (f0.size, self.neq))

    def solve(self, time_points, terminate=None):
        """
        Compute solution u for t values in the list/array
        time_points, as long as terminate(u,t,step_no) is False.
        terminate(u,t,step_no) is a user-given function
        returning True or False. By default, a terminate
        function which always returns False is used.
        """
        if terminate is None:
            terminate = lambda u, t, step_no: False

        if isinstance(time_points, (float,int)):
            raise TypeError('solve: time_points is not a sequence')
        self.t = np.asarray(time_points)
        if self.t.size <= 1:
            raise ValueError('ODESolver.solve requires time_points array with at least 2 time points')

        n = self.t.size
        if self.neq == 1:  # scalar ODEs
            self.u = np.zeros(n)
        else:              # systems of ODEs
            self.u = np.zeros((n,self.neq))

        # Assume that self.t[0] corresponds to self.U0
        self.u[0] = self.U0

        # Time loop
        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
            if terminate(self.u, self.t, self.k+1):
                break  # terminate loop over k
        return self.u[:k+2], self.t[:k+2]


class ForwardEuler(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        u_new = u[k] + dt*f(u[k], t[k])
        return u_new

class RungeKutta4(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        dt2 = dt/2.0
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + dt2)
        K3 = dt*f(u[k] + 0.5*K2, t[k] + dt2)
        K4 = dt*f(u[k] + K3, t[k] + dt)
        u_new = u[k] + (1/6.0)*(K1 + 2*K2 + 2*K3 + K4)
        return u_new
    
#--------------------------------------------------------------------------------------
#Class for root finding from Unit 9, exercise 17
#--------------------------------------------------------------------------------------

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
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
#Class for numerical differentiation from Unit 9, exercise 18
#--------------------------------------------------------------------------------------
class Diff2:
    def __init__(self, f, h=1E-5, dfdx_exact=None):
        self.f = f
        self.h = float(h)
        self.exact = dfdx_exact

    def error(self, x):
        if self.exact is not None:
            df_numerical = self(x)
            df_exact = self.exact(x)
            return df_exact - df_numerical

class Forward1(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h

class Backward1(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h

class Central2(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)

class Central4(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (4./3)*(f(x+h)   - f(x-h))  /(2*h) - \
               (1./3)*(f(x+2*h) - f(x-2*h))/(4*h)

class Central6(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (3./2) *(f(x+h)   - f(x-h))  /(2*h) - \
               (3./5) *(f(x+2*h) - f(x-2*h))/(4*h) + \
               (1./10)*(f(x+3*h) - f(x-3*h))/(6*h)

class Forward3(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (-(1./6)*f(x+2*h) + f(x+h) - 0.5*f(x) - \
                (1./3)*f(x-h))/h
    
class Backward2(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x-2*h)-4*f(x-h)+3*f(x))/(2*h)
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------


#Here starts the actual E18 problem:

class Inverse:
    def __init__(self,f,I,x0=None,resolution=1000):
        """The interval I is given in terms of the original function:
        Inverse(sin(x), I=[0, pi/2]) will get the interval I for sin so that the interval for the 
        inverse is [0,1]. Note that the inverse for sin is not defined in [0, pi/2].
        So I'd recommend not to provide x0 at all"""
        
        self.f,self.I,self.res=f,I,resolution
        if x0 is None:
            x0=f(I[0])
        xf=f(I[1])
        if x0<xf: #f increasing
            self.x0=x0
            self.xf=xf
            self.initialval=I[0] #invf(x0)=I0
        else: #f decreasing
            self.x0=xf
            self.xf=x0
            self.initialval=I[1] #invf(self.x0=xf)=I1
            
        
    def compute(self):
        #define ODE problem
        dfdx=Central2(self.f)
        rhs=lambda x,t: 1/dfdx(x)
        frk=RungeKutta4(rhs)
        #Set initial condition
        frk.set_initial_condition(self.initialval)  
        #Set interval for inverse and solve
        tpoints=np.linspace(self.x0,self.xf,1+self.res) 
        solRK, tRK = frk.solve(tpoints)
        return tRK, solRK
    
    
def test_Inverse():
    """Check that class Inverse is correct in finfind the inverse of y=2x"""
    f=lambda x:2*x
    inverse = Inverse(f, I=[0,10], resolution=100)
    x, y = inverse.compute()
    y_expected=0.5*x
    assert np.allclose(y,y_expected), "Obtained result is not the expected"



if __name__ == '__main__':  
    test_Inverse()
    
    def f(x):
        return np.sin(x)
    def invf(x):
        return np.arcsin(x)
    interval=[0, 0.5*np.pi]
    
    plt.figure()
    inverse = Inverse(f, I=interval, resolution=100)
    x, y = inverse.compute()
    plt.plot(x, y, "r-", label="Numerical inverse")
    #correct value        
    yok=invf(x)
    plt.plot(x, yok, "b:", label="Analytical inverse")  
    #ogfunc 
    xog=np.linspace(interval[0],interval[1],1001)
    yog=f(xog)
    plt.plot(xog, yog, "g-", label="y=sin(x)")  
    plt.plot(xog, xog, "k:", label="Reflection symmetry axis x=y")
    plt.legend()
    plt.axis([0,1.6,0,1.6])
    plt.title("Function and inverse")
    plt.savefig("ejE18a.png")
    
    
    
    interval=[0.5, 1.5]
    plt.figure()
    inverse = Inverse(f, I=interval, resolution=100)
    x, y = inverse.compute()
    plt.plot(x, y, "r-", label="Numerical inverse")
    #correct value        
    yok=invf(x)
    plt.plot(x, yok, "b:", label="Analytical inverse")  
    #ogfunc 
    xog=np.linspace(interval[0],interval[1],1001)
    yog=f(xog)
    plt.plot(xog, yog, "g-", label="y=sin(x)")  
    plt.plot(xog, xog, "k:", label="Reflection symmetry axis x=y")
    plt.legend()
    plt.axis([0.4,1.6,0.4,1.6])
    plt.title("Function and inverse")
    plt.savefig("ejE18b.png")
    
    def f(x):
        return -np.sin(x)
    def invf(x):
        return np.arcsin(-x)
    
    plt.figure()
    interval=[0, 1.5]
    inverse = Inverse(f, I=interval, resolution=100)
    x, y = inverse.compute()
    plt.plot(x, y, "r-", label="Numerical inverse")
    #correct value        
    yok=invf(x)
    plt.plot(x, yok, "b:", label="Analytical inverse")  
    #ogfunc 
    xog=np.linspace(interval[0],interval[1],1001)
    yog=f(xog)
    plt.plot(xog, yog, "g-", label="y=-sin(x)")
    xref=np.linspace(-1.5,1.5,31)
    plt.plot(xref, xref, "k:", label="Reflection symmetry axis x=y")
    plt.legend()
    plt.axis([-1,1.5,-1,1.5])
    plt.title("Function and inverse")
    plt.savefig("ejE18c.png")
    
    
    def f(x):
        return x**2
    def invf(x):
        return np.sqrt(x)
    
    plt.figure()
    interval=[0.001, 1.5]
    inverse = Inverse(f, I=interval, resolution=10000) #since f'(I0)~0, we have to increase the resolution
    x, y = inverse.compute()
    plt.plot(x, y, "r-", label="Numerical inverse")
    #correct value        
    yok=invf(x)
    plt.plot(x, yok, "b:", label="Analytical inverse")  
    #ogfunc 
    xog=np.linspace(interval[0],interval[1],1001)
    yog=f(xog)
    plt.plot(xog, yog, "g-", label="y=x²")
    xref=np.linspace(-1.5,1.5,31)
    plt.plot(xref, xref, "k:", label="Reflection symmetry axis x=y")
    plt.legend()
    plt.axis([-0.1,2.3,-0.1,2.3])
    plt.title("Function and inverse")
    plt.savefig("ejE19a.png")
    
    def f(x):
        return 1-np.sqrt(x)
    def invf(x):
        return (1-x)**2
    
    plt.figure()
    interval=[0.001, 1.5]
    inverse = Inverse(f, I=interval, resolution=100) #f'(I0)~inf, we can work with this resolution
    x, y = inverse.compute()
    plt.plot(x, y, "r-", label="Numerical inverse")
    #correct value        
    yok=invf(x)
    plt.plot(x, yok, "b:", label="Analytical inverse")  
    #ogfunc 
    xog=np.linspace(interval[0],interval[1],1001)
    yog=f(xog)
    plt.plot(xog, yog, "g-", label="y=1-sqrt(x)")
    xref=np.linspace(-1.5,1.5,31)
    plt.plot(xref, xref, "k:", label="Reflection symmetry axis x=y")
    plt.legend()
    plt.axis([-0.25,1.55,-0.25,1.55])
    plt.title("Function and inverse")
    plt.savefig("ejE19b.png")
    #plt.show()
    
    
    
    
