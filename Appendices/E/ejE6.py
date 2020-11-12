"""ODE for emptying a tank"""
import numpy as np
import matplotlib.pyplot as plt

#Superclass with every particular method as a subclass
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



#Parameters
r=1
R=20
g=9.81
h0=1

def f(h,t):
    print ("h",h)
    print(-(r/R)**2*np.sqrt(2*g*h))
    return -(r/R)**2*np.sqrt(2*g*h)

T=200
dt=10
n=int(T/dt)+1
tpoints=np.linspace(0,n*dt,n+1)

#Plot exact solution
def h_exact(t):
    a=np.sqrt(h0)-(r/R)**2*np.sqrt(0.5*g)*t
    result=np.where(a>0,a**2,0) #When a=0 the tank is empty and remains empty
    return result

tgrid=np.linspace(0,T,2001)
hexact=h_exact(tgrid)
plt.plot(tgrid, hexact, "k-", label="Exact Solution")


#Numerical calculations and plots
def terminate(h,t,step_no): #stop calculations if h<=0, or nan (may happen in RK for big dt, when h<0 may enter to f)
    eps=1e-6
    return ((h[step_no])<eps or np.isnan(h[step_no]))
    
fEuler=ForwardEuler(f=f)
fEuler.set_initial_condition(h0)
sol, t = fEuler.solve(tpoints, terminate)
plt.plot(t, sol, "--", label="Euler dt=%g"%(t[1]-t[0]))

rk4=RungeKutta4(f=f)
rk4.set_initial_condition(U0=h0)
sol, t = rk4.solve(tpoints, terminate)
plt.plot(t, sol, "-.", label="4° order Runge-Kutta dt=%g"%(t[1]-t[0]))


plt.legend()
#plt.title("")
plt.axis([-10,max(t)+5,-0.05,1.05])
plt.xlabel("t")
plt.ylabel("h(t)")
plt.savefig("ejE6.png")

