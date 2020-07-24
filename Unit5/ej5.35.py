"Heatwave movie (function T(z,t))"

from math import pi, sqrt, log
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def T(z, t):
    # T0, A1, A2, a1, a2 and omega are global variables
    return T0 + A1*np.exp(-a1*z)*np.sin(omega1*t - a1*z) +A2*np.exp(-a2*z)*np.sin(omega2*t - a2*z) 

import glob, os
# Remove old plot files
for filename in glob.glob('ej5.35hw_*.png'): os.remove(filename)

k = 1E-6     # thermal diffusivity (in m**2/s)
P2 = 24*60*60.# oscillation period of 24 h (in seconds)
P1=P2*365 # oscillation period of a year (in seconds)
omega1 = 2*pi/P1
omega2 = 2*pi/P2
dt = P2/10    # time lag: 2.4 h
tmax = P1/50   # ~1 week simulations
T0 = 10      # mean surface temperature in Celsius
A1 = 15       # amplitude of the anual temperature variations (in C)
A2 = 7       # amplitude of the daily temperature variations (in C)
a1 = sqrt(omega1/(2*k))
a2 = sqrt(omega2/(2*k))
D = -(0.7/a1)*log(0.001) # max depth
n = 501      # no of points in the z direction



z = np.linspace(0, D, n)
tlist=np.linspace(0,tmax,int(tmax/dt)+1)
# Make a first plot (save the lines objects returned from plt.plot)
fig = plt.figure()
plt.axis([z[0], z[-1], T0-A1-A2, T0+A1+A2])
lines = plt.plot([],[])
plt.xlabel("depth [m]")
plt.ylabel("T [°C]")
plt.title("T(z) in a week, dt=2.4 h")
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
    lines[0].set_label('t=%4.2f h ' %(t/3600.0))
    plt.legend()
    plt.savefig('ej5.35hw_%04d.png' % frame_no)
    return lines

all_args = [(frame_no, t, z, lines)
            for frame_no, t in enumerate(tlist)]

# Run the animation
anim = animation.FuncAnimation(
    fig, frame, all_args, interval=150, init_func=init, blit=True)

# Make movie file in MP4 format
anim.save("ej5.35hw.mp4", fps=6)
plt.show()

## Make movie files in .gif
os.system('convert -delay 50 ej5.35hw_*.png ej5.35hw.gif')
## Can use ffmpeg instead of avconv
