def random_walk_2D(np, ns):
    moves = numpy.random.normal(0, 0.05, size=2*(ns+1)*np)   #Normal dist. with mean 0 and s.d. 0.05
    moves.shape = ((ns+1), np, 2) #((ns+1)*np) for x and y, extra step to include initial position of zeros
    moves[0,:,:]=0 #Initially all particles are in (0;0)
    #position[i][j][0]=x-position of particle j+1 on step i+1, position[i][j][1]=y-position of particle j+1 on step i+1
    positions=numpy.cumsum(moves, axis=0) #cumulative sum on moves over steps (1st index), for each particle and direction
    return positions

    
def makemovie(pos):  #part b
    framenum=min(101,len(pos[:,0,0])) #do all steps or 101, whichever is lower
    
    import glob, os
    # Remove old plot files
    for filename in glob.glob('ej8.35_*.png'): os.remove(filename)
    
    # Make a first plot (save the lines objects returned from plt.plot)
    fig = plt.figure()
    plt.axis([-numpy.sqrt(framenum/20),numpy.sqrt(framenum/20),-numpy.sqrt(framenum/20),numpy.sqrt(framenum/20)]) #works ok for several ns
    lines = plt.plot([],[],"ko") 
    
    # Function to return the background plot in the animation
    def init():
        lines[0].set_data([],[])  # empty plot
        return lines
    
    def frame(args):
        frame_no, pos, lines = args
        x=pos[frame_no,:,0]
        y=pos[frame_no,:,1]
        lines[0].set_data(x, y)
        lines[0].set_label('t=%g s' %frame_no)
        plt.legend(loc=1) #location upper right
        plt.title("Randm walk")
        plt.savefig('ej8.35_%04d.png' % frame_no)
        return lines
    
    all_args = [(frame_no, pos, lines)
                 for frame_no in range(framenum)]
    
    anim = animation.FuncAnimation(
    fig, frame, all_args, interval=150, init_func=init, blit=True)
    
    # Make movie file in MP4 format
    anim.save("ej8.35rw.mp4", fps=8)

    ## Make movie files in .gif
    os.system('convert -delay 10 ej8.35_*.png ej8.35rw.gif')
    

def meandist(pos): #part c
    dist=numpy.sqrt(pos[:,:,0]*pos[:,:,0]+pos[:,:,1]*pos[:,:,1]) #dist(i,j)=distance form the origin of particle j+1 on step i+1
    meandist=numpy.sum(dist,axis=1) #sum over particles
    meandist/=len(dist[0,:]) #divide by number of particles
    return meandist


    
# Main program
import matplotlib.pyplot as plt
import numpy, sys
import matplotlib.animation as animation
#numpy.random.seed(11)

np = int(sys.argv[1])  # number of particles
ns = int(sys.argv[2])  # number of steps
r = random_walk_2D(np, ns)
makemovie(r)
mean=meandist(r)

#part c plot
plt.figure()
time=numpy.linspace(0,ns,ns+1)
expect=0.062*numpy.sqrt(time) #expected~sqrt(ns), factor found by examination
plt.plot(time,mean,"o",label="average distance")
plt.plot(time,expect,"r-.",label="expected~sqrt(N)")
plt.legend()
plt.title("Average distance form the origin over time")
plt.xlabel("Step")
plt.ylabel("Average distance to origin [mm]")
plt.savefig("ej8.35c.png")
