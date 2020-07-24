from math import sqrt, sin, cos, pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def pathlength(x, y):
    if len(x)!=len(y):
        print ("both argumets must have the same number of elements!")
        return
    else:
      leng=0.0
      for i in range(1,len(x)):
          leng+=sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
      return leng

def pointgen(n):
    """generates a set of n+1 points on a circumference with radius 1/2"""
    x=[0.5*cos(2*pi*i/n) for i in range(n+1)]
    y=[0.5*sin(2*pi*i/n) for i in range(n+1)]
    return x, y


def piapprox(k):
    xk, yk = pointgen(k)
    lenk=pathlength(xk, yk)
    error= abs(pi-lenk)
    return xk, yk, error

    
import glob, os
# Remove old plot files
for filename in glob.glob('ej5.37pi_*.png'): os.remove(filename)

# Make a first plot (save the lines objects returned from plt.plot)
fig = plt.figure()
plt.axis([-0.6, 0.6, -0.6, 0.6])
xcf=[0.5*cos(2*pi*i/10000) for i in range(10001)]
ycf=[0.5*sin(2*pi*i/10000) for i in range(10001)]
plt.plot(xcf,ycf,"-") #fixed background circumference
plt.axis("equal") #to make the circumference not look as an elipse.
lines = plt.plot([],[],"o-") 
#plt.xlabel("")
#plt.ylabel("")
#plt.title("")

# Function to return the background plot in the animation
def init():
    lines[0].set_data([],[])  # empty plot
    return lines

def frame(args):
    frame_no, k, lines = args
    x, y, err=piapprox(k)
    lines[0].set_data(x, y)
    #lines[0].set_label('k=%g' %k)
    #plt.legend()
    plt.title("Absolute error in the approximation for k=%g: %5.4f" %(k,err))
    plt.savefig('ej5.37pi_%04d.png' % frame_no)
    return lines

kmax=100 #max. number of points
all_args = [(frame_no, k, lines)
            for frame_no, k in enumerate(range(4,kmax))]

# Run the animation
anim = animation.FuncAnimation(
    fig, frame, all_args, interval=300, init_func=init, blit=True)

# Make movie file in MP4 format
anim.save("ej5.37pi.mp4", fps=1)

## Make movie files in .gif
os.system('convert -delay 50 ej5.37pi_*.png ej5.37pi.gif')
plt.show()

