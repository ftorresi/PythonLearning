"""ODE for an object falling"""
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


#u'=f(u,t) as a class
class f:
    def __init__(self, rho_b, A, V, C, rho=0, g=9.81):
        self.rho_b, self.A, self.V, self.C, self.rho, self.g=rho_b, A, V, C, rho, g
    
    def __call__(self,u,t):
        rho_b, A, V, C, rho, g=self.rho_b, self.A, self.V, self.C, self.rho, self.g
        dv=-g*(1-rho/rho_b)-0.5*C*rho*A*u*abs(u)/(rho_b*V)
        return dv
    

###Part b:

def test_freefall():
    #Parameters
    rho_b=1003 #Falling body density
    A=0.2 #Falling body cross-section (circular area of r=25cm)
    V=0.08 #Falling body volume
    C=0.6 #drag coefficient
    rho=0 #fluid density=0 --> Only gravity force
    g=9.81 #gravity acceleration  
    
    #exact solution
    def vb_exact(t,v0=0):
        return v0-g*t
    
    #v0 T and dt
    v0=11 
    T=2*v0/g
    dt=0.1
    n=int(T/dt)+1

    #plot exact solution:
    plt.figure()
    tgrid=np.linspace(0,n*dt,2001)
    vexact=vb_exact(tgrid,v0)
    plt.plot(tgrid, vexact, "k-", label="Exact Solution")

    #Numerical solution
    tpoints=np.linspace(0,n*dt,n+1)
    f_init=f(rho_b, A, V, C, rho, g)
    fEuler=ForwardEuler(f=f_init)
    fEuler.set_initial_condition(v0)
    sol, t = fEuler.solve(tpoints)
    plt.plot(t, sol, "--", label="Euler dt=%g"%(t[1]-t[0]))

    plt.legend()
    plt.title("Only gravitational force")
    plt.xlabel("t")
    plt.ylabel("v(t)")
    plt.savefig("ejE9b.png")
    
    v_expected=vb_exact(tpoints,v0)
    assert np.allclose(v_expected, sol, rtol=1E-14), "Numerical solution not close enough to exact solution"
    
    #Check also the expected numerical values, v[k]=v0-k*g*dt
    v_discrete=v0-np.arange(len(sol))*g*dt
    assert np.allclose(v_discrete, sol, rtol=1E-14), "Obtained numerical solution not close enough to expected numerical solution"

#test_freefall()

    
####Part c   

def plotforces(t,v,rho_b, A, V, C, rho=0, g=9.81):
    
    fg=np.zeros_like(t)
    fg+=-rho_b*V*g #constant
    
    fb=np.zeros_like(t)
    fb+=rho*g*V #constant
    
    fd=-0.5*C*rho*A*np.abs(v)*v
    
    #plt.figure()
    plt.plot(t, fg, "r-",label="Gravitational Force")
    plt.plot(t, fd, "b-",label="Drag Force")
    plt.plot(t, fb, "g-",label="Buoyancy")
    plt.legend()
    plt.xlabel("t")
    plt.ylabel("Forces (t)")
    plt.title("Forces acting on the object")
    #plt.savefig("ejE9-forces.png")

    
###Part d
#Terminate simulation when a constant velocity is reached
def term(v,t,step):
    eps=1e-6
    return abs(v[step]-v[step-1])<eps

#Parameters
rho_b=1003 #Falling body density
A=0.2 #Falling body cross-section (circular area of r=25cm)
V=0.08 #Falling body volume
C=0.6 #drag coefficient
rho=0.79 #fluid density
g=9.81 #gravity acceleration

#v0 T and dt
v0=0 
T=400 #In a free fall, it would take ~32s to hit the ground so this T is more than enough
dt=0.1
n=int(T/dt)+1

#Numerical solution
tpoints=np.linspace(0,n*dt,n+1)
f_init=f(rho_b, A, V, C, rho, g)
plt.figure()

#Euler
fEuler=ForwardEuler(f=f_init)
fEuler.set_initial_condition(v0)
solE, tE = fEuler.solve(tpoints,term)
plt.plot(tE, solE, "--", label="Euler dt=%g"%(tE[1]-tE[0]))

#Runge-Kutta 4° order
frk=RungeKutta4(f=f_init)
frk.set_initial_condition(v0)
solRK, tRK = frk.solve(tpoints,term)
plt.plot(tRK, solRK, "--", label="4° order Runge-Kutta dt=%g"%(tRK[1]-tRK[0]))

plt.legend()
plt.title("Skydiver velocity")
plt.xlabel("t")
plt.ylabel("v(t)")
plt.savefig("ejE9d.png")

plt.figure()
#plotforces(tE,solE,rho_b, A, V, C, rho, g)
plotforces(tRK,solRK,rho_b, A, V, C, rho, g)
plt.savefig("ejE9d-forces.png")

#Terminal velocity vs dt
dts=[19,18,17,16,15,14,10,5,1,0.1]
termvel=[]
for dt in dts:
    n=int(T/dt)+1
    tpoints=np.linspace(0,n*dt,n+1) 
    frk=RungeKutta4(f=f_init)
    frk.set_initial_condition(v0)
    solRK, tRK = frk.solve(tpoints,term)
    termvel.append(solRK[-1])
vterm_exact=-np.sqrt(abs((rho-rho_b)*g*V)/(0.5*C*rho*A))
plt.figure()
plt.plot(dts,np.full_like(dts,vterm_exact),"r--", label="Exact value")
plt.plot(dts,termvel,"bo:", label="Numerical calculations")
plt.axis([0,max(dts)+1,-129,-110])
plt.legend()
plt.title("Limit velocity vs step size")
plt.xlabel("dt")
plt.ylabel("terminal velocity")
plt.savefig("ejE9d-termvel.png")



###Part e

#Parameters
rho_b=77.13 #Falling body density
A=0.038 #Falling body cross-section (circular area of r=25cm)
V=0.0056 #Ball volume
C=0.4 #drag coefficient
rho=1000 #fluid density
g=9.81 #gravity acceleration

#v0 T and dt
v0=0 
T=1
dt=0.002
n=int(T/dt)+1


#Numerical solution
tpoints=np.linspace(0,n*dt,n+1)
f_init=f(rho_b, A, V, C, rho, g)
plt.figure()

#Euler
fEuler=ForwardEuler(f=f_init)
fEuler.set_initial_condition(v0)
solE, tE = fEuler.solve(tpoints,term)
plt.plot(tE, solE, "--", label="Euler dt=%g"%(tE[1]-tE[0]))

#Runge-Kutta 4° order
frk=RungeKutta4(f=f_init)
frk.set_initial_condition(v0)
solRK, tRK = frk.solve(tpoints,term)
plt.plot(tRK, solRK, "--", label="4° order Runge-Kutta dt=%g"%(tRK[1]-tRK[0]))

plt.legend()
plt.title("Submerged ball velocity")
plt.xlabel("t")
plt.ylabel("v(t)")
plt.savefig("ejE9e.png")

plt.figure()
#plotforces(tE,solE,rho_b, A, V, C, rho, g)
plotforces(tRK,solRK,rho_b, A, V, C, rho, g)
plt.savefig("ejE9e-forces.png")

#Terminal velocity vs dt
dts=[0.001*i for i in range(1,31)]
termvel=[]
for dt in dts:
    n=int(T/dt)+1
    tpoints=np.linspace(0,n*dt,n+1) 
    frk=RungeKutta4(f=f_init)
    frk.set_initial_condition(v0)
    solRK, tRK = frk.solve(tpoints,term)
    termvel.append(solRK[-1])
vterm_exact=np.sqrt(abs((rho-rho_b)*g*V)/(0.5*C*rho*A))
plt.figure()
plt.plot(dts,np.full_like(dts,vterm_exact),"r--", label="Exact value")
plt.plot(dts,termvel,"bo:", label="Numerical calculations")
plt.axis([-0.002,max(dts)+0.002,2.582,2.583])
plt.legend()
plt.title("Limit velocity vs step size")
plt.xlabel("dt")
plt.ylabel("terminal velocity")
plt.savefig("ejE9e-termvel.png")
