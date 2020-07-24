import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time, glob, os

#Vectorized version of funcion in ej3.30
def H_eps_vec(x,eps=0.01):
    condition1=np.logical_and(-eps<=x , x<=eps)
    condition2=x>eps
    
    r=np.zeros_like(x)
    r[condition1]=0.5+x[condition1]/(2*eps)+np.sin(np.pi*x[condition1]/eps)/(2*np.pi)
    r[condition2]=1.0
    return r


x=np.linspace(-3,3,1001)
emax=2.0
emin=0.01
elist=np.linspace(emax,emin,41)
    

#Clean up old frames
for name in glob.glob("Heps_*.png"):
    os.remove(name)


# Make a first plot (save the lines objects returned from plt.plot)
fig = plt.figure()
plt.axis([x[0], x[-1], -0.05, 1.05])
lines = plt.plot([],[])
plt.xlabel("x")
plt.ylabel("H(x,eps)")
#plt.legend(["eps="])

# Function to return the background plot in the animation
def init():
    lines[0].set_data([], [])  # empty plot
    return lines

# Function to return a frame in the movie
def frame(args):
    frame_no, eps, x, lines = args
    y = H_eps_vec(x, eps)
    lines[0].set_data(x, y)
    lines[0].set_label('eps=%4.2f' %eps)
    plt.legend()
    plt.savefig('Heps_%04d.png' % frame_no)
    return lines

# Construct list of all arguments to frame function
# (each call sends frame number, eps value, x array, and lines list)
all_args = [(frame_no, eps, x, lines)
            for frame_no, eps in enumerate(elist)]

# Run the animation
anim = animation.FuncAnimation(
    fig, frame, all_args, interval=150, init_func=init, blit=True)

# Make movie file in MP4 format
anim.save("ej34Heps.mp4", fps=6)
plt.show()

