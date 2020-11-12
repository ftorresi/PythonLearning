"""Function implementing the Forward Euler method for scalar ODEs."""
import numpy as np

def ForwardEuler(f, U0, T, n):
    """Solve u'=f(u,t), u(0)=U0, with n steps until t=T."""
    t = np.zeros(n+1)
    u = np.zeros(n+1)  # u[k] is the solution at time t[k]
    u[0] = U0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t



#Two verifications
def test_ForwardEuler_against_hand_calculations():
    """Verify ForwardEuler against hand calc. for 3 time steps in u'=u."""
    def f(u, t):
         return u
    u, t = ForwardEuler(f, U0=1, T=0.2, n=2)
    exact = np.array([1, 1.1, 1.21])  # hand calculations
    error = np.abs(exact - u).max()
    success = error < 1E-14
    assert success, '|exact - u| = %g != 0' % error

def test_ForwardEuler_against_linear_solution():
    """Use knowledge of an exact numerical solution for testing."""
    def f(u, t):
        return 0.2 + (u - u_exact(t))**4

    def u_exact(t):
        return 0.2*t + 3

    u, t = ForwardEuler(f, U0=u_exact(0), T=3, n=5)
    u_e = u_exact(t)
    error = np.abs(u_e - u).max()
    success = error < 1E-14
    assert success, '|exact - u| = %g != 0' % error

if __name__ == '__main__':
    #Make 2 tests
    test_ForwardEuler_against_hand_calculations()
    test_ForwardEuler_against_linear_solution()
    
    #Solve problem: u'=u as a demo
    def f(u, t):
        return u

    u, t = ForwardEuler(f, U0=1, T=4, n=20)

    # Compare numerical solution and exact solution in a plot
    import matplotlib.pyplot as plt
    u_exact = np.exp(t)
    plt.plot(t, u_exact, 'b-',label="exact")
    plt.plot(t, u, 'r-',label="numerical")
    plt.legend()
    plt.xlabel('t')
    plt.ylabel('u')
    plt.title("Solution of the ODE u'=u, u(0)=1")
    plt.savefig("ejE15.png")
