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
    
    
class Problem:
    def __init__(self,h,Ts,T0,dt):
        self.h,self.Ts,self.T0,self.dt=h,Ts,T0,dt
        
    def __call__(self,u,t):
        return -self.h*(u-self.Ts)

    
    def termination(self, u, t, step_no):
        """Return True when asymptotic value Ts is reached."""
        tol = 0.01 #Stop when solution is 0.01°C close to asymptotic value Ts
        return abs(u[step_no]- self.Ts) < tol
    
def estimate_h(t1, T0, T1, Ts):
    return (T1-T0)/(t1*(Ts-T0))

def test_Problem():
    Ts=20
    templist=np.linspace(0,100,201)
    for h in range(10):
        p=Problem(h=h,Ts=Ts,T0=100,dt=1)
        pt=p(templist,0)
        assert np.allclose(pt, -h*(templist-Ts)) #compare with expected value
        
def solve(prob):
    """Solve with Runge-Kutta 4° order"""
    frk=RungeKutta4(prob)
    frk.set_initial_condition(prob.T0)
    n=5000/dt+1
    tpoints=np.linspace(0,n*dt,int(n))
    solRK, tRK = frk.solve(tpoints,problem.termination)
    plt.plot(tRK, solRK, "--", label="4° order Runge-Kutta dt=%g, Ts=%g"%((tRK[1]-tRK[0]),prob.Ts))
    
    
    
if __name__ == '__main__':
    test_Problem()
    ##Parameters
    Ts=20
    T0=200
    T1=180
    t1=50
    happ=estimate_h(t1, T0, T1, Ts) 
    dt=10
    
    problems = {T_0: [Problem(happ, T_s, T_0, dt) for T_s in (15, 22, 30)] for T_0 in (250, 200)}
    for T_0 in problems:
        plt.figure()
        for problem in problems[T_0]:
            solve(problem)
        plt.legend()
        plt.title("Newton law of cooling, T0=%g, h=%g"%(T_0, happ))
        plt.xlabel("t [s]")
        plt.ylabel("T [°C]")
        #plt.show()
        plt.savefig("ejE13_T0=%g.png"% T_0)
        #savefig(’T0_%g’.pdf % T_0)






#f_init=f(h_approx,Ts)
#tpoints=np.linspace(0,5000,126)


#def termination(u, t, step_no):
    #"""Return True when asymptotic value Ts is reached."""
    #tol = 0.01 #Stop when solution is 0.01°C close to asymptotic value Ts
    #return abs(u[step_no]- Ts) < tol
    
##Euler
#fEuler=ForwardEuler(f_init)
#fEuler.set_initial_condition(T0)
#solE, tE = fEuler.solve(tpoints,termination)
#plt.plot(tE, solE, "--", label="Euler dt=%g"%(tE[1]-tE[0]))

##Runge-Kutta 4° order
#frk=RungeKutta4(f_init)
#frk.set_initial_condition(T0)
#solRK, tRK = frk.solve(tpoints,termination)
#plt.plot(tRK, solRK, "--", label="4° order Runge-Kutta dt=%g"%(tRK[1]-tRK[0]))

##exact solution
#def T_exact(t,h,Tamb,Ti):
    #return Tamb+(Ti-Tamb)*np.exp(-h*t)
#exact=T_exact(tRK,h=h_approx,Tamb=Ts, Ti=T0)
#plt.plot(tRK, exact, "k:", label="Analytical Solution")

#plt.legend()
#plt.title("Newton law of cooling, T0=%g, Ts=%g, h=%g"%(T0, Ts, h_approx))
#plt.xlabel("t [s]")
#plt.ylabel("T [°C]")
#plt.savefig("ejE12.png")
#plt.show()
