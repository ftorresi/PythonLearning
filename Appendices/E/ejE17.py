"""ODE for the inverse of a function"""
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


#Here starts the actual E17 problem:

#Define the right side of the ODE as a class:

class FunctionToInvert:
    def __init__(self,f, xr=None,dfdx=None):
        self.f=f
        
        if dfdx is None:   #If f' not given, evaluate numerically with, e.g., Central2
            dfdx=Central2(f)
        self.dfdx=dfdx
                
        if xr is None:  #If xr not given, evaluate numerically with, e.g., Newton
            nroot=Newton(f,dfdx)
            xr,yr,xrlist,yrlist,n,boolean=nroot.solve()
        self.xr=xr
        
    def __call__(self,u,t):
        return 1/self.dfdx(u)

    
#Initialize:
tpoints=np.linspace(0,10,101)
xder=FunctionToInvert(lambda x: 2*x) 
plt.figure()

#Runge-Kutta 4° order
frk=RungeKutta4(xder)
frk.set_initial_condition(xder.xr)
solRK, tRK = frk.solve(tpoints)
plt.plot(tRK, solRK, "r-", label="Inverse, dt=%g"%(tRK[1]-tRK[0]))

##Original function
og=2*tpoints
plt.plot(tpoints, og, "b-", label="Original y=2*x")
##Reflection symmetry axis
plt.plot(tpoints, tpoints, "k:", label="Reflection symmetry axis x=y")
plt.legend()
plt.title("Function and inverse")
plt.axis([0,10,0,10])
plt.savefig("ejE17a.png")


#-------------------------------------------------
#Initialize:

def sqrtder(t):
    return 0.5/np.sqrt(t)

tpoints=np.linspace(0,10,10001)
xder=FunctionToInvert(np.sqrt,1e-12,sqrtder) #can't use the exact xr=0 or the numerical method since 1/sqrt(0) would appear
plt.figure()

#Runge-Kutta 4° order
frk=RungeKutta4(xder)
frk.set_initial_condition(xder.xr)
solRK, tRK = frk.solve(tpoints)
plt.plot(tRK, solRK, "r-", label="Inverse, dt=%g"%(tRK[1]-tRK[0]))

##Original function
og=np.sqrt(tpoints)
plt.plot(tpoints, og, "b-", label="Original y=sqrt(x)")
##Reflection symmetry axis
plt.plot(tpoints, tpoints, "k:", label="Reflection symmetry axis x=y")
plt.legend()
plt.title("Function and inverse")
plt.axis([0,10,0,10])
plt.savefig("ejE17b.png")
#plt.show()

