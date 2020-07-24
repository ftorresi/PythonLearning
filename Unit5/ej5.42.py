from math import pi
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#Vectorized S
def S(t,n=10,T=2*pi):
    suma=0.0
    for i in range(1,n+1):
        suma+=(1.0/(2*i-1))*np.sin(2*(2*i-1)*pi*t/float(T))
    suma*=4/np.pi
    return suma

#Vectorized piecewise function    
def fvec(t,T=2*pi):
    condition1=np.logical_and(0<t,t<0.5*T)
    condition2=np.logical_and(0.5*T<t,t<T)
    
    r=np.zeros_like(t)
    r[condition1]=1.0
    r[condition2]=-1.0
    return r
    
T0=2*pi    
tgrid=np.linspace(0,T0,501)
tlist=tgrid[1:-1] #since f(0) and f(T) are not defined
nmax=50
nlist=range(1,nmax+1)


import glob, os
# Remove old plot files
for filename in glob.glob('ej5.42pw_*.png'): os.remove(filename)


# Make a first plot (save the lines objects returned from plt.plot)
fig = plt.figure()
plt.axis([0, T0, -1.3, 1.3])
lines = plt.plot([],[],"r-.") 
y=fvec(tlist,T0)
plt.plot(tlist,y,"k-") #Exact function as background
plt.xlabel("t")
plt.ylabel("S")
plt.title("Step function and its approximations with n sin terms")
#plt.show()

# Function to return the background plot in the animation
def init():
    lines[0].set_data([],[])  # empty plot
    return lines

def frame(args):
    frame_no, n, T0, tlist, lines = args
    z=S(tlist,n,T0)
    lines[0].set_data(tlist, z)
    lines[0].set_label('n=%d' %n)
    plt.legend()
    plt.savefig('ej5.42pw_%04d.png' % frame_no)
    return lines

all_args = [(frame_no, n, T0, tlist, lines)
            for frame_no, n in enumerate(nlist)]

# Run the animation
anim = animation.FuncAnimation(
    fig, frame, all_args, interval=150, init_func=init, blit=True)

# Make movie file in MP4 format
anim.save("ej5.42pw.mp4", fps=8)

## Make movie files in .gif
os.system('convert -delay 30 ej5.42pw_*.png ej5.42pw.gif')
plt.show()

