
def random_walk_2D(np, ns, plot_step, xmin=None, xmax=None, ymin=None, ymax=None):
    if xmin==None: xmin=-ns
    if ymin==None: ymin=-ns
    if xmax==None: xmax=ns
    if ymax==None: ymax=ns
    
    #Start uniformly distributed
    xp=numpy.linspace(0,99,100)
    yp=numpy.linspace(0,199,200)
    xpositions, ypositions = numpy.meshgrid(xp, yp)
    xpositions=numpy.reshape(xpositions,20000) #give a 1D shape
    ypositions=numpy.reshape(ypositions,20000)
    
    #Save positions to make movie later
    xhistory=[xpositions]
    yhistory=[ypositions]
    
    moves = numpy.random.random_integers(1, 4, size=ns*np)
    moves.shape = (ns, np)

    for step in range(ns):
        this_move = moves[step,:]
        ypositions += numpy.where(this_move == 1, 1, 0)
        ypositions = numpy.where(ypositions>ymax,ymax,ypositions) #Put back particle inside box
        ypositions -= numpy.where(this_move == 2, 1, 0)
        ypositions = numpy.where(ypositions<ymin,ymin,ypositions) #Put back particle inside box
        xpositions += numpy.where(this_move == 4, 1, 0)
        xpositions = numpy.where(xpositions>xmax,xmax,xpositions) #Put back particle inside box
        xpositions -= numpy.where(this_move == 3, 1, 0)        
        xpositions = numpy.where(xpositions<xmin,xmin,xpositions) #Put back particle inside box
        
        # Just plot every plot_step steps
        if (step+1) % plot_step == 0:
            xhistory.append(xpositions)
            yhistory.append(ypositions)

    return xhistory, yhistory


def makemovie(posx, posy):  #part b
    framenum=len(posx)

    import glob, os
    # Remove old plot files
    for filename in glob.glob('ej8.39_*.png'): os.remove(filename)
    
    # Make a first plot (save the lines objects returned from plt.plot)
    fig = plt.figure()
    xbox=[0,0,199,199,0]; ybox=[0,199,199,0,0]
    plt.axis([0,199,0,199]) #BOX
    plt.plot(xbox,ybox,"b-",linewidth=4) 
    lines = plt.plot([],[],"ko",markersize=2) 
    
    # Function to return the background plot in the animation
    def init():
        lines[0].set_data([],[])  # empty plot
        return lines
    
    def frame(args):
        frame_no, posx, posy, lines = args
        x=posx[frame_no]
        y=posy[frame_no]
        lines[0].set_data(x, y)
        lines[0].set_label('step=%g' %(frame_no*10))
        plt.legend(loc=1) #location upper right
        plt.title("Randm walk")
        plt.savefig('ej8.39_%04d.png' % frame_no)
        return lines
    
    all_args = [(frame_no, posx, posy, lines)
                 for frame_no in range(framenum)]
    
    anim = animation.FuncAnimation(
    fig, frame, all_args, interval=150, init_func=init, blit=True)
    
    # Make movie file in MP4 format
    anim.save("ej8.39rw.mp4", fps=8)

    ## Make movie files in .gif
    os.system('convert -delay 10 ej8.39_*.png ej8.39rw.gif')
    
    
# Main program
import numpy, sys
#numpy.random.seed(11)

np = 20000  # number of particles #This np is better suited for this exercise
ns = 1000  # number of steps
x, y = random_walk_2D(np, ns, 10, 0,199,0,199) #Box [0,199]x[0,199], plot each 10 steps
import matplotlib.pyplot as plt
import matplotlib.animation as animation
makemovie(x, y)
