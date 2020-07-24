#from numpy import *
#from matplotlib.pyplot import * 
#def f1(t):
    #return t**2*exp(-t**2)
#def f2(t):
    #return t**4*exp(-t**2)

#t = linspace(0, 3, 51)
#y1 =f1(t)
#y2 =f2(t)

#plot(t, y1, "r-")
##hold("on") #deprecated. plot commands add elements without first clearing the axes and/or figure. To plot in different graphs, use figure().
#plot(t, y2, "bo")

#xlabel("t")
#ylabel("y")
#legend(["t^2*exp(-t^2)","t^4*exp(-t^2)" ])
#axis([-0, 3, -0.05, 0.6]) # [tmin, tmax, ymin, ymax]
#title("My First Matplotlib Demo")
##savefig("tmp1.pdf") # produce PDF
##savefig("tmp1.png") # produce PNG
##show()


##!!!!! multiple plots #!!!!!
#figure() # make separate figure
#subplot(2, 1, 1) #2 rows 1 column, 1° plot

#plot(t, y1, "r-", t, y2, "bo")
#xlabel("t")
#ylabel("y")
#axis([t[0], t[-1], min(y2)-0.05, max(y2)+0.051])
#legend(["t^2*exp(-t^2)", "t^4*exp(-t^2)"])
#title("Top figure")

#subplot(2, 1, 2) #2 rows 1 column, 2° plot
#t3 = t[::4]
#y3 = f2(t3)

#plot(t, y1, "r--", t3, y3, "ys")
#legend(["t^2*exp(-t^2)", "t^4*exp(-t^2)"])
#xlabel("t")
#ylabel("y")
#axis([0, 3.1, -0.2, 0.6])
##title("Bottom figure")
#show()

#!!!! Make a Movie !!!!#

#import numpy as np
#import matplotlib.pyplot as plt
#import time, glob, os

## Clean up old frames
#for name in glob.glob("tmp_*.pdf"):
    #os.remove(name)

#def f(x, m, s):
    #return (1.0/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

#m = 0
#s_max = 2
#s_min = 0.2
#x = np.linspace(m -3*s_max, m + 3*s_max, 1000)
#s_values = np.linspace(s_max, s_min, 30)
## f is max for x=m; smaller s gives larger max value
#max_f = f(m, m, s_min)

## Make a first plot (here empty)
#plt.ion()
#y = f(x, m, s_max)
#lines = plt.plot(x, y)
#plt.axis([x[0], x[-1], -0.1, max_f])
#plt.xlabel("x")
#plt.ylabel("f")
#plt.legend(["s=%4.2f" % s_max])

## Show the movie, and make hardcopies of frames simulatenously
#counter = 0
#for s in s_values:
    #y = f(x, m, s)
    #lines[0].set_ydata(y)
    #plt.legend(["s=%4.2f" % s])
    #plt.draw()
    #plt.savefig("tmp_%04d.png" % counter)
    #counter += 1
#input("Type Return key: ")

#!!!! Make a Movie - better version !!!!#

#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#import time, glob, os

#def f(x, m, s):
    #return (1.0/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

#m = 0
#s_max = 2
#s_min = 0.2
#x = np.linspace(m -3*s_max, m + 3*s_max, 1000)
#s_values = np.linspace(s_max, s_min, 30)
## f is max for x=m; smaller s gives larger max value
#max_f = f(m, m, s_min)

## Make a first plot (save the lines objects returned from plt.plot)
#fig = plt.figure()
#plt.axis([x[0], x[-1], -0.1, max_f])
#lines = plt.plot([], [])
#plt.xlabel("x")
#plt.ylabel("f")

## Function to return the background plot in the animation
#def init():
    #lines[0].set_data([], [])  # empty plot
    #return lines

## Function to return a frame in the movie
#def frame(args):
    #frame_no, s, x, lines = args
    #y = f(x, m, s)
    #lines[0].set_data(x, y)
    ## Does not work: lines[0].set_label("s=%4.2f" % s)
    ## Does not work: plt.legend(["s=%4.2f" % s])
    ## Does not work: plt.savefig("tmp_%04d.png" % frame_no)
    #return lines

## Construct list of all arguments to frame function
## (each call sends frame number, s value, x array, and lines list)
#all_args = [(frame_no, s, x, lines)
            #for frame_no, s in enumerate(s_values)]

## Run the animation
#anim = animation.FuncAnimation(
    #fig, frame, all_args, interval=150, init_func=init, blit=True)

## Make movie file in MP4 format
#anim.save("movie1.mp4", fps=5)
#plt.show()


##!!!! Make a 3D plot !!!!#
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

h0=2277 #[m]
R=4 #[km]

x = y = np.linspace(-10., 10., 41)
xv, yv = np.meshgrid(x, y, indexing="ij", sparse=False) #2D grid
hv = h0/(1 + (xv**2+yv**2)/(R**2)) #z=f(x,y)

#parametrized curve
s = np.linspace(0, 2*np.pi, 100)
curve_x = 10*(1 - s/(2*np.pi))*np.cos(s)
curve_y = 10*(1 - s/(2*np.pi))*np.sin(s)
curve_z = h0/(1 + 100*(1 - s/(2*np.pi))**2/(R**2))

###3D
fig = plt.figure(1) # Get current figure
ax = fig.gca(projection="3d") # Get current axes
ax.plot_wireframe(xv, yv, hv, rstride=2, cstride=2) #wireframe plot

# Simple plot of mountain and parametric curve
fig = plt.figure(2)
ax = fig.gca(projection="3d")
from matplotlib import cm #colormap
ax.plot_surface(xv, yv, hv,cmap=cm.seismic,
rstride=1, cstride=1)

# add the parametric curve. linewidth controls the width of the curve
ax.plot(curve_x, curve_y, curve_z, linewidth=5)


###CONTOUR
# Default two-dimensional contour plot with 7 colored lines
fig = plt.figure(3)
ax = fig.gca()
ax.contour(xv, yv, hv)
plt.axis("equal")

# Default three-dimensional contour plot
fig = plt.figure(4)
ax = fig.gca(projection="3d")
ax.contour(xv, yv, hv)

# Plot of mountain and contour lines projected
# coordinate planes
fig = plt.figure(5)
ax = fig.gca(projection="3d")
ax.plot_surface(xv, yv, hv, cmap=cm.coolwarm,
rstride=1, cstride=1)
# zdir is the projection axis
# offset is the offset of the projection plane
ax.contour(xv, yv, hv, zdir="z", offset=-1000,cmap=cm.coolwarm)
ax.contour(xv, yv, hv, zdir="x", offset=-10,cmap=cm.coolwarm)
ax.contour(xv, yv, hv, zdir="y", offset=10,cmap=cm.coolwarm)

# View the contours by displaying as an image
fig = plt.figure(6)
ax = fig.gca()
ax.imshow(hv)

# 10 contour lines (equally spaced contour levels)
fig = plt.figure(7)
ax = fig.gca()
ax.contour(xv, yv, hv, 10)
plt.axis("equal")

# 10 black ("k") contour lines
fig = plt.figure(8)
ax = fig.gca()
ax.contour(xv, yv, hv, 10, colors="k")
plt.axis("equal")

# Specify the contour levels explicitly as a list
fig = plt.figure(9)
ax = fig.gca()
levels = [500., 1000., 1500., 2000.]
ax.contour(xv, yv, hv, levels=levels)
plt.axis("equal")

# Add labels with the contour level for each contour line
fig = plt.figure(10)
ax = fig.gca()
cs = ax.contour(xv, yv, hv)
plt.clabel(cs)
plt.axis("equal")

##Gradient Field
#Make less dense grid
x2 = y2 = np.linspace(-10.,10.,11)
x2v, y2v = np.meshgrid(x2, y2, indexing="ij", sparse=False)
h2v = h0/(1 + (x2v**2 + y2v**2)/(R**2)) # h on coarse grid
#Evaluate gradient
dhdx, dhdy = np.gradient(h2v) # dh/dx, dh/dy

#Plot vector field
fig = plt.figure(11)
ax = fig.gca()
ax.quiver(x2v, y2v, dhdx, dhdy, color="r",
angles="xy", scale_units="xy")
ax.contour(xv, yv, hv)
plt.axis("equal")

plt.show()


