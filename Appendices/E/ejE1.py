"""This exercise aims to solve the ODE problem u - 10u' = 0  u(0)= 0.2 in [0,20]"""
import numpy as np
import matplotlib.pyplot as plt

#Exact solution
def exact_u(t):
    return 0.2*np.exp(0.1*t)

#u'=f(u,t)
def f(u,t):
    return 0.1*u    

#Forward Euler Method
def ForwardEuler(f, U0, T, n):
    """Solve u’=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.linspace(0,T,n+1)
    u = np.zeros(n+1) # u[k] is the solution at time t[k]
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t

#Parameters
T=20
U0=0.2

#Plot exact solution
tgrid=np.linspace(0,T,2001)
uexact=exact_u(tgrid)
plt.plot(tgrid, uexact, "r-", label="Exact Solution")


#Numerical calculations and plots
nlist=[4,40,400]
for n in nlist:
    sol, t=ForwardEuler(f=f, U0=U0, T=T, n=n)
    plt.plot(t, sol, "--", label="dt=%g"%(t[1]-t[0]))


plt.legend()
plt.title("u-10u'=0, u(0)=0.2")
plt.xlabel("t")
plt.ylabel("u(t)")
plt.savefig("ejE1.png")

#Save to file (only last solution)
with open("ejE1.out","w") as outfile:
    outfile.write("Numerical Solution to u-10u'=0, u(0)=0.2 \n")
    outfile.write(" t    u(t)\n")
    for i in range(len(t)):
        outfile.write("%5.2f  %7.4f\n"%(t[i], sol[i]))
