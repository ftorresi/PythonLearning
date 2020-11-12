"""Now we solve the ODE problem u - 10u' = 0  u(0)= 0.2 in [0,20] using HEUN's method"""
import numpy as np
import matplotlib.pyplot as plt

#Exact solution
def exact_u(t):
    return 0.2*np.exp(0.1*t)

#u'=f(u,t) as a class
class f:
    def __init__(self):
        pass
    
    def __call__(self,u,t):
        return 0.1*u


#Forward Euler Method as a class
class Heun:
    def __init__(self, f, U0, T, n):
        if not callable(f):
            raise TypeError('f is %s, not a function' % type(f))
        self.f, self.U0, self.T, self.n = f, U0, T, n
        self.dt = T/float(n)
        self.u = np.zeros(n+1)
        self.t = np.linspace(0,T,n+1)
        
    def solve(self):
        """Compute solution for 0 <= t <= T."""
        self.u[0] = float(self.U0)
        for k in range(self.n):
            self.k = k
            self.u[k+1] = self.advance()
        return self.u, self.t
    
    def advance(self):
        """Advance the solution one time step."""
        u, dt, f, k, t = self.u, self.dt, self.f, self.k, self.t
        f_eval=f(u[k], t[k])
        u_mid= u[k] + dt*f_eval
        u_new = u[k] + 0.5*dt*(f_eval+f(u_mid, t[k+1]))
        return u_new


#Parameters
T=20
U0=0.2

#Plot exact solution
tgrid=np.linspace(0,T,2001)
uexact=exact_u(tgrid)
plt.plot(tgrid, uexact, "r-", label="Exact Solution")


#Numerical calculations and plots
nlist=[4,40,400]
f_init=f()
for n in nlist:
    solver=Heun(f=f_init, U0=U0, T=T, n=n)
    sol, t = solver.solve()
    plt.plot(t, sol, "--", label="dt=%g"%(t[1]-t[0]))


plt.legend()
plt.title("u-10u'=0, u(0)=0.2 with Heun's method")
plt.xlabel("t")
plt.ylabel("u(t)")
plt.savefig("ejE5.png")

#Save to file (only last solution)
with open("ejE5.out","w") as outfile:
    outfile.write("Numerical Solution to u-10u'=0, u(0)=0.2 with Heun's method\n")
    outfile.write(" t    u(t)\n")
    for i in range(len(t)):
        outfile.write("%5.2f  %7.4f\n"%(t[i], sol[i]))
