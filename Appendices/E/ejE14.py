"""ODE for cooling of an object"""
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

#Making u=(T-Ts)/(T0-Ts), tau=t*h, the ODE is now du/dtau=-u, u(0)=1
class f:
    def __init__(self):
        pass
        
    def __call__(self,u,t):
        return -u 


def termination(u, t, step_no):
    """Return True when asymptotic value Ts is reached."""
    tol = 0.001 #Stopping threshold
    return abs(u[step_no]) < tol

def solveRK():
    U0=1
    f_init=f()
    tpoints=np.linspace(0,10,101)
    #Runge-Kutta 4° order
    frk=RungeKutta4(f_init)
    frk.set_initial_condition(U0)
    solRK, tRK = frk.solve(tpoints,termination)
    return solRK, tRK


def load():
    #Load solution    
    with open("ejE14.dat","r") as infile:    
        u=[]    
        tau=[]    
        for line in infile:    
            data=line.split()    
            tau.append(float(data[0]))    
            u.append(float(data[1]))
    return tau, u


def T(u, tau, h, T0, Ts):
    #Rescale using parameters:
    tau=np.asarray(tau)
    u=np.asarray(u)
    time=(1/h)*tau
    Temp=Ts+(T0-Ts)*u
    return time, Temp
    

import os
#If solution was not previously calculated, do it
if not os.path.isfile("ejE14.dat"):
    uarr, tauarr=solveRK()
    with open("ejE14.dat","w") as outfile:
        for t,u in zip(tauarr,uarr):
            outfile.write("%.3f   %g\n"%(t,u))
            
#load solution
tau, u=load()

#read parameters from command line
import sys
try:
    h=float(sys.argv[1])
    Ts=float(sys.argv[2])
    T0=float(sys.argv[3])
except:
    print("usage: %s h Ts T0" %sys.argv[0])
    sys.exit(1)

#rescale
t, T= T(u,tau,h,T0,Ts)
#plot
plt.plot(t, T, "r--",label="T0=%g, Ts=%g, h=%g"%(T0, Ts, h))
plt.title("Newton law of cooling")
plt.legend()
plt.xlabel("t [s]")
plt.ylabel("T [°C]")
plt.savefig("ejE14.png")
plt.show()





