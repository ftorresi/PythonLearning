import ODESolver
from matplotlib.pyplot import plot, figure, savefig, title, show
#from matplotlib.pyplot import plot, figure, savefig, title, show
import numpy as np

class Problem:
    def __init__(self, alpha, R, U0, T):
        """
        alpha, R: parameters in the ODE.
        U0: initial condition.
        T: max length of time interval for integration;
        asympotic value R must be reached within 1%
        accuracy for some t <= T.
        """
        self.alpha, self.R, self.U0, self.T = alpha, R, U0, T

    def __call__(self, u, t):
        """Return f(u,t) for logistic ODE."""
        return self.alpha*u*(1 - u/self.R)

    def terminate(self, u, t, step_no):
        """Return True when asymptotic value R is reached."""
        tol = self.R*0.01
        return abs(u[step_no] - self.R) < tol

    def __str__(self):
        """Pretty print of physical parameters."""
        return 'alpha=%g, R=%g, U0=%g' % \
               (self.alpha, self.R, self.U0)

class Solver:
    def __init__(self, problem, dt,
                 method=ODESolver.ForwardEuler):
        """
        problem: instance of class Problem.
        dt: time step.
        method: class in ODESolver hierarchy.
        """
        self.problem, self.dt = problem, dt
        self.method = method

    def solve(self):
        solver = self.method(self.problem)
        solver.set_initial_condition(self.problem.U0)
        n = int(round(self.problem.T/self.dt))
        t_points = np.linspace(0, self.problem.T, n+1)
        self.u, self.t = solver.solve(t_points,
                                      self.problem.terminate)

        # The solution terminated if the limiting value was reached
        if solver.k+1 == n:  # no termination - we reached final T
            self.plot()
            raise ValueError(
                'termination criterion not reached, '\
                'give T > %g' % self.problem.T)

    def plot(self):
        filename = 'logistic_' + str(self.problem) + '.pdf'
        plot(self.t, self.u)
        title(str(self.problem) + ', dt=%g' % self.dt)
        savefig(filename)
        show()


def find_dt(problem, method=ODESolver.ForwardEuler,
            tol=0.01, dt_min=1E-6):
    """
    Return a "solved" class Solver instance where the
    difference in the solution and one with a double
    time step is less than tol.
    problem: class Problem instance.
    method: class in ODESolver hierarchy.
    tol: tolerance (chosen relative to problem.R).
    dt_min: minimum allowed time step.
    """
    dt = problem.T/10  # start with 10 intervals
    solver = Solver(problem, dt, method)
    solver.solve()

    good_approximation = False
    print("Using a poor version of find_dt. Ideally dt should be given to AutoSolver")
    while not good_approximation:
        dt = dt/2.0
        if dt < dt_min:
            raise ValueError('dt=%g < %g - abort' % (dt, dt_min))

        solver2 = Solver(problem, dt, method)
        solver2.solve()

        ## Make continuous functions u(t) and u2(t)
        #NOT AVAILABLE
        #u  = wrap2callable((solver. t, solver. u))
        #u2 = wrap2callable((solver2.t, solver2.u))

        ## Sample the difference in n points in [0, t_end]
        #n = 13
        #t_end = min(solver2.t[-1], solver.t[-1])
        #t = np.linspace(0, t_end, n)
        #u_diff = np.abs(u(t) - u2(t)).max()
        #print (u_diff, dt, tol)
        
        #As wrap2callable is not available, I simplify the test
        u_diff=abs(solver.u[-1]-solver2.u[-1]) #Hoping the final ts are not too different...
        print (u_diff, dt, tol)
        
        if u_diff < tol:
            good_approximation = True
        else:
            solver = solver2
    return solver2


class AutoSolver(Solver):
    def __init__(self, problem, dt=None,
                 method=ODESolver.ForwardEuler,
                 tol=0.01, dt_min=1E-6):
        Solver.__init__(self, problem, dt, method)
        if dt is None:
            solver = find_dt(self.problem, method,
                             tol, dt_min)
            self.dt = solver.dt
            self.u, self.t = solver.u, solver.t

    def solve(self, method=ODESolver.ForwardEuler):
        if hasattr(self, 'u'):
            # Solution was computed by find_dt in constructor
            pass
        else:
            Solver.solve(self)



class Problem2(Problem):
    def __init__(self, alpha, R, U0, T):
        """
        alpha, R: parameters in the ODE.
        U0: initial condition.
        T: max length of time interval for integration;
        asympotic value R must be reached within 1%
        accuracy for some t <= T.
        """
        self.alpha, self.U0, self.T = alpha, U0, T
        if isinstance(R, (float,int)):  # number?
            self.R = lambda t: R
        elif callable(R):
            self.R = R
        else:
            raise TypeError(
                'R is %s, has to be number of function' % type(R))

    def __call__(self, u, t):
        """Return f(u,t) for logistic ODE."""
        return self.alpha*u*(1 - u/self.R(t))

    def terminate(self, u, t, step_no):
        """Return True when asymptotic value R is reached."""
        #tol = self.R(t[step_no])*0.01
        #return abs(u[step_no] - self.R(t[step_no])) < tol
        return False   

    def __str__(self):
        return 'alpha=%g, U0=%g' % (self.alpha, self.U0)



if __name__ == '__main__':
    def Rvar(t,ts=5):
        if t<ts:
            return 500
        elif t<2*ts:
            return 200
        else:
            return Rvar(t-2*ts)
    
    problem = Problem2(alpha=0.1, U0=2, T=500, R=Rvar) #I disable the terminate function in Problem2 so as to see the oscilations
    solver = AutoSolver(problem, dt=0.5)
    solver.solve(method=ODESolver.RungeKutta4)
    print ('dt:', solver.dt)
    solver.plot()
    
        
