import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import factorial

def v(r,n=1):
    R=1 #pipe radius
    b=0.02 #pressure gradient
    mu=0.02 #viscosity coeff.
    return (b/(2*mu))**(1./n)*(float(n)/(n+1))*(R**(1+1.0/n)-r**(1+1.0/n))


x=np.linspace(0,1,501)
y=v(x,n=0.1)
plt.plot(x,y,"k-")
plt.xlabel("r")
plt.ylabel("v")
plt.axis([0, 1, 0, 1e-4])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0)) #use scientific notation on y axis
plt.title("      Fluid velocity on a pipe, from centerline to pipe wall")
plt.savefig('ej5.40b.png')

import glob, os
# Remove old plot files
for filename in glob.glob('ej5.40vp_*.png'): os.remove(filename)


# Make a first plot (save the lines objects returned from plt.plot)
nlist=np.linspace(0.01,1,51)
fig = plt.figure()
plt.axis([0, 1, 0, 1.01])
lines = plt.plot([],[],"r-") 
plt.xlabel("r")
plt.ylabel("v/v0")
plt.title("Fluid velocity on a pipe, from centerline to pipe wall, for different n")
#plt.show()

# Function to return the background plot in the animation
def init():
    lines[0].set_data([],[])  # empty plot
    return lines

def frame(args):
    frame_no, n, x, lines = args
    y=v(x,n)
    y/=v(0.0,n) #Normalize
    lines[0].set_data(x, y)
    lines[0].set_label('n=%4.3f' %n)
    plt.legend()
    plt.savefig('ej5.40vp_%04d.png' % frame_no)
    return lines

all_args = [(frame_no, n, x, lines)
            for frame_no, n in enumerate(nlist)]

# Run the animation
anim = animation.FuncAnimation(
    fig, frame, all_args, interval=150, init_func=init, blit=True)

# Make movie file in MP4 format
anim.save("ej5.40vp.mp4", fps=8)

## Make movie files in .gif
os.system('convert -delay 30 ej5.40vp_*.png ej5.40vp.gif')
#plt.show()
