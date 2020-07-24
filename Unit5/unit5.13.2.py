"Heatwave movie (function T(z,t))"

from math import pi, sqrt, cos, log, exp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def T(z, t):
    # T0, A, k, and omega are global variables
    a = sqrt(omega/(2*k))
    return T0 + A*np.exp(-a*z)*np.cos(omega*t - a*z)

import glob, os
# Remove old plot files
for filename in glob.glob('Tw_*.png'): os.remove(filename)

k = 1E-6     # thermal diffusivity (in m**2/s)
P = 24*60*60.# oscillation period of 24 h (in seconds)
omega = 2*pi/P
dt = P/24    # time lag: 1 h
tmax = 3*P   # 3 day/night simulations
T0 = 10      # mean surface temperature in Celsius
A = 10       # amplitude of the temperature variations (in C)
a = sqrt(omega/(2*k))
D = -(1/a)*log(0.001) # max depth
n = 501      # no of points in the z direction



z = np.linspace(0, D, n)
tlist=np.linspace(0,tmax,int(tmax/dt)+1)
# Make a first plot (save the lines objects returned from plt.plot)
fig = plt.figure()
plt.axis([z[0], z[-1], T0-A, T0+A])
lines = plt.plot([],[])
plt.xlabel("depth [m]")
plt.ylabel("T [°C]")
#plt.legend(["t="])

# Function to return the background plot in the animation
def init():
    lines[0].set_data([], [])  # empty plot
    return lines

# Function to return a frame in the movie
def frame(args):
    frame_no, t, z, lines = args
    y = T(z, t)
    lines[0].set_data(z, y)
    lines[0].set_label('t=%4.2f h' %(t/3600.0))
    plt.legend()
    plt.savefig('Tw_%04d.png' % frame_no)
    return lines

all_args = [(frame_no, t, z, lines)
            for frame_no, t in enumerate(tlist)]

# Run the animation
anim = animation.FuncAnimation(
    fig, frame, all_args, interval=150, init_func=init, blit=True)

# Make movie file in MP4 format
anim.save("Tw.mp4", fps=6)
plt.show()

## Make movie files in .gif
os.system('convert -delay 50 Tw_*.png Tw.gif')
## Can use ffmpeg instead of avconv
