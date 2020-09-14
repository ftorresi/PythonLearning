#Idem 8.39 but instead of removing the division, we make a 'small hole'
def random_walk_2D(np, ns, plot_step, xmin=None, xmax=None, ymin=None, ymax=None, hz=10):
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
    
    #hole position:
    yhmin=100-int(hz/2) #max=100, and below
    yhmax=99+round(hz/2) #min=100, and above
    #particles can pass through x=100 if they have yhmin<=y<=yhmax
    
    #Save positions to make movie later
    xhistory=[xpositions]
    yhistory=[ypositions]
    
    moves = numpy.random.random_integers(1, 4, size=ns*np)
    moves.shape = (ns, np)

    for step in range(ns):
        this_move = moves[step,:]
        ypositions += numpy.where(this_move == 1, 1, 0)
        ypositions = numpy.where(ypositions>ymax,ymax,ypositions) #Put back particle inside box
        #Check hole transition
        c_x100=xpositions==100  #Get which particles are trying to pass the wall
        yind=numpy.zeros_like(ypositions, dtype=int) #Array like ypositions filled with 0
        yind[c_x100]=1 #Array with 1 where particles try to pass wall, 0 otherwise
        yind[ypositions>yhmax]+=1 # If it passes the wall, has an 1, 2 if it does not
        ypositions-=numpy.where(yind==2,1,0) #Go back only if didn't pass wall
        
        ypositions -= numpy.where(this_move == 2, 1, 0)
        ypositions = numpy.where(ypositions<ymin,ymin,ypositions) #Put back particle inside box
        #Check hole transition
        c_x100=xpositions==100  #Get which particles are trying to pass the wall
        yind=numpy.zeros_like(ypositions, dtype=int) #Array like ypositions filled with 0
        yind[c_x100]=1 #Array with 1 where particles try to pass wall, 0 otherwise
        yind[ypositions<yhmin]+=1 # If it passes the wall, has an 1, 2 if it does not
        ypositions+=numpy.where(yind==2,1,0) #Go back only if didn't pass wall
        
        xpositions += numpy.where(this_move == 4, 1, 0)
        xpositions = numpy.where(xpositions>xmax,xmax,xpositions) #Put back particle inside box
        #Check hole transition
        c_x100=xpositions==100  #Get which particles are trying to pass the wall
        yind=numpy.zeros_like(ypositions, dtype=int) #Array like ypositions filled with 0
        yind[c_x100]=1 #Array with 1 where particles try to pass wall, 0 otherwise
        yind[ypositions>yhmax]+=1 # If it passes the wall, has an 1, 2 if it does not
        yind[ypositions<yhmin]+=1
        xpositions-=numpy.where(yind==2,1,0) #Go back only if didn't pass wall
        
        xpositions -= numpy.where(this_move == 3, 1, 0)        
        xpositions = numpy.where(xpositions<xmin,xmin,xpositions) #Put back particle inside box
        #Check hole transition
        c_x100=xpositions==100  #Get which particles are trying to pass the wall
        yind=numpy.zeros_like(ypositions, dtype=int) #Array like ypositions filled with 0
        yind[c_x100]=1 #Array with 1 where particles try to pass wall, 0 otherwise
        yind[ypositions>yhmax]+=1 # If it passes the wall, has an 1, 2 if it does not
        yind[ypositions<yhmin]+=1
        xpositions+=numpy.where(yind==2,1,0) #Go back only if didn't pass wall

        
        # Just plot every plot_step steps
        if (step+1) % plot_step == 0:
            xhistory.append(xpositions)
            yhistory.append(ypositions)

    return xhistory, yhistory


def makemovie(posx, posy, hz):  #part b
    framenum=len(posx)

    import glob, os
    # Remove old plot files
    for filename in glob.glob('ej8.40_*.png'): os.remove(filename)
    
    # Make a first plot (save the lines objects returned from plt.plot)
    fig = plt.figure()
    plt.axis([0,199,0,199]) #BOX
    #hole position:
    yhmin=100-int(hz/2) #max=100, and below
    yhmax=99+round(hz/2) #min=100, and above
    xbox=[100,100,0,0,199,199,100]; ybox=[yhmax,199,199,0,0,199,199]
    plt.plot(xbox,ybox,"b-",linewidth=5) #BOX+upper wall
    xw=[100,100]; yw=[0,yhmin]
    plt.plot(xw,yw,"b-",linewidth=5) #lower wall
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
        plt.title("Random walk for a gas through a hole")
        plt.savefig('ej8.40_%04d.png' % frame_no)
        return lines
    
    all_args = [(frame_no, posx, posy, lines)
                 for frame_no in range(framenum)]
    
    anim = animation.FuncAnimation(
    fig, frame, all_args, interval=150, init_func=init, blit=True)
    
    # Make movie file in MP4 format
    anim.save("ej8.40rw.mp4", fps=8)

    ## Make movie files in .gif
    os.system('convert -delay 10 ej8.40_*.png ej8.40rw.gif')
    
    
# Main program
import numpy, sys
#numpy.random.seed(11)

np = 20000  # number of particles #This np is better suited for this exercise
ns = 1000  # number of steps
hz=20 #hole size
x, y = random_walk_2D(np, ns, 10, 0,199,0,199,hz) #Box [0,199]x[0,199], plot each 10 steps
import matplotlib.pyplot as plt
import matplotlib.animation as animation
makemovie(x, y, hz)
