def init_prms(m, b, L, k, beta, S0, dt, g, w_formula, N):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--m', '--mass',
                        type=float, default=m)
    parser.add_argument('--b', '--boxheight',
                        type=float, default=b)
    parser.add_argument('--L', '--spring-length',
                        type=float, default=L)
    parser.add_argument('--k', '--spring-stiffness',
                        type=float, default=k)
    parser.add_argument('--beta', '--spring-damping',
                        type=float, default=beta)
    parser.add_argument('--dt','--timestep',
                        type=float, default=dt)
    parser.add_argument('--g', '--gravity',
                        type=float, default=g)
    parser.add_argument('--S0', '--initial-position', type=str, default=str(S0)) #So that S0 can be an expression of other parameters (ex: m*g/k)
    parser.add_argument('--w', type=str, default=w_formula)
    parser.add_argument('--N', type=int, default=N)
    args = parser.parse_args()

    from scitools.StringFunction import StringFunction
    w = StringFunction(args.w, independent_variables='t')
    return args.m, args.b, args.L, args.k, args.beta, \
           args.S0, args.dt, args.g, w, args.N


def solve(m, k, beta, S0, dt, g, w, N,
          user_action=lambda S, time, time_step_no: None):
    """Calculate N steps forward. Return list S."""
    S = [0.0]*(N+1)      # output list
    gamma = beta*dt/2.0  # short form
    t = 0
    S[0] = S0
    user_action(S, t, 0)
    # Special formula for first time step
    i = 0
    S[i+1] = (1/(2.0*m))*(2*m*S[i] - dt**2*k*S[i] +
             m*(w(t+dt) - 2*w(t) + w(t-dt)) + dt**2*m*g)
    t = dt
    user_action(S, t, i+1)

    # Time loop
    for i in range(1,N):
        S[i+1] = (1/(m + gamma))*(2*m*S[i] - m*S[i-1] +
                                  gamma*dt*S[i-1] - dt**2*k*S[i] +
                                  m*(w(t+dt) - 2*w(t) + w(t-dt))
                                  + dt**2*m*g)
        t += dt
        user_action(S, t, i+1)

    return S

def demo():
    def print_S(S, t, step):
        """Callback function: user_action."""
        print ('t=%.2f  S[%d]=%+g' % (t, step, S[step]))

    from math import pi

    m, b, L, k, beta, S0, dt, g, w, N = \
       init_prms(m=1, b=2, L=10, k=1, beta=0, S0=0,
                 dt=2*pi/40, g=9.81, w_formula='0', N=80)
    S0=eval(S0) #So that S0 can be an expression of other parameters (ex: m*g/k)

    S = solve(m, k, beta, S0, dt, g, w, N,
              user_action=print_S)

    import matplotlib.pyplot as plt
    import numpy as np
    time=np.linspace(0,N*dt,N+1)
    plt.plot(time,S)
    title="g=%g, S0=%g, w=2 in [20;30], 0 otherwise" %(g,S0)
    plt.title(title)
    plt.ylabel("spring stretch [m]")
    plt.xlabel("time [s]")
    plt.show()
    
def plotall():
    from math import pi
    import numpy as np
    import matplotlib.pyplot as plt

    m, b, L, k, beta, S0, dt, g, w, N = \
       init_prms(m=1, b=2, L=10, k=1, beta=0, S0=0,
                 dt=2*pi/40, g=9.81, w_formula='0', N=80)
    S0=eval(S0) #So that S0 can be an expression of other parameters (ex: m*g/k)

    S = solve(m, k, beta, S0, dt, g, w, N)
    
    # Vectorize the StringFunction w
    w_formula = str(w)  # keep this to see if w=0 later
    if ' else ' in w_formula:
        w = np.vectorize(w)        # general vectorization
    else:
        w.vectorize(globals())  # more efficient (when no if)
    

    time=np.linspace(0,N*dt,N+1)
    S=np.asarray(S)

    
    plots = 2         # number of rows of plots
    if beta != 0:
        plots += 1
    if w_formula != '0':
        plots += 1

    # Position Y(t)
    plot_row = 1
    plt.subplot(plots, 1, plot_row)
    Y = w(time) - L - S - b/2.0
    plt.plot(time, Y)
    plt.ylabel("Position Y [m]")
    
    # Spring force (and S)
    plot_row += 1
    plt.subplot(plots, 1, plot_row)
    Fs = k*S
    plt.plot(time, Fs)
    plt.ylabel("Spring force [N]")
    
    # Friction force
    if beta != 0:
        plot_row += 1
        plt.subplot(plots, 1, plot_row)
        Fd = beta*np.diff(S)  # diff is in numpy
        # len(diff(S)) = len(S)-1 so we use time[:-1]:
        plt.plot(time[:-1], Fd)
        plt.ylabel("Friction force [N]")
    
    # Excitation
    if w_formula != '0':
        plot_row += 1
        plt.subplot(plots, 1, plot_row)
        w_array = w(time)
        plt.plot(time, w_array)
        plt.xlabel("time [s]")
        plt.ylabel("Excitation [m]")
    
    plt.savefig('ejD3.png')  # save this multi-axis plot in a file


if __name__ == '__main__':
    plotall()
    #run for exercise using: """python ejD3.py  --w "1 if t>0 else 0" --N 300 --S0 "m*g/k"
    #We get oscilations of Y around Y0=w-L-0.5*b-S0=-10-g~-19.8

"""WARNING: The numerical solution exhibits a non-physical behaviuor: for S0=mg/k, w=0, the solution should be S(t)=mg/k for all t, whatever beta we choose. However if we set beta>0, the numerical solution goes S-->0"""











































































