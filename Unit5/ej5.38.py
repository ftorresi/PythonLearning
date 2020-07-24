import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def position(t):
    x=a*np.cos(w*t)
    y=b*np.sin(w*t)
    return x, y


def velocity(t):
    return w*np.sqrt((a*np.sin(w*t))**2+(b*np.cos(w*t))**2)

w=1 
a=1.3
b=1 
tmax=2*np.pi/w
tlist=np.linspace(0,tmax,73) #one point every 5°
#x, y=position(t)
#v=velocity(t)

import glob, os
# Remove old plot files
for filename in glob.glob('ej5.38po_*.png'): os.remove(filename)


# Make a first plot (save the lines objects returned from plt.plot)
fig = plt.figure()
#plt.axis([-a, a, -b, b])
tel=np.linspace(0,tmax,361) #one point every 1° to draw elipse
xel, yel=position(tel)
plt.plot(xel,yel,"k-.") #fixed background elipse
plt.axis("equal") #to make the elipse look as such.
lines = plt.plot([],[],"ro", markersize=12) 
#plt.xlabel("")
#plt.ylabel("")
#plt.show()

# Function to return the background plot in the animation
def init():
    lines[0].set_data([],[])  # empty plot
    return lines

def frame(args):
    frame_no, t, lines = args
    x, y=position(t)
    v=velocity(t)
    lines[0].set_data(x, y)
    #lines[0].set_label('k=%g' %k)
    #plt.legend()
    plt.title("Planet's velocity= %5.4f" %v)
    plt.savefig('ej5.38po_%04d.png' % frame_no)
    return lines

all_args = [(frame_no, t, lines)
            for frame_no, t in enumerate(tlist)]

# Run the animation
anim = animation.FuncAnimation(
    fig, frame, all_args, interval=150, init_func=init, blit=True)

# Make movie file in MP4 format
anim.save("ej5.38po.mp4", fps=8)

## Make movie files in .gif
os.system('convert -delay 30 ej5.38po_*.png ej5.38po.gif')
plt.show()

