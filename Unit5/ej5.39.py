import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import factorial

def animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact):
    


    import glob, os
    # Remove old plot files
    for filename in glob.glob('ej5.39Te_*.png'): os.remove(filename)
    
    
    # Make a first plot (save the lines objects returned from plt.plot)
    fig = plt.figure()
    plt.axis([xmin, xmax, ymin, ymax])
    x=np.linspace(xmin,xmax,n) 
    yexact=exact(x) #exact function
    klist=np.array(range(M,N+1)) #array of k-values
    plt.plot(x,yexact,"k-") #fixed background exact function
    lines = plt.plot([],[],"r-.") 
    #plt.xlabel("x")
    #plt.ylabel("")
    #plt.show()
   
#NOTE: I had to use this k-loop since doing taylorsum+=fk(x,k) inside frame, for an initial taylorsum=np.zeros_like(x) had a bug   
    taylorsum=np.zeros((N-M+1,n))
    for k in klist:
        if k==0:
            taylorsum[k]=fk(x,M+k)
        else:
            taylorsum[k]=fk(x,M+k)+taylorsum[k-1]
            

    # Function to return the background plot in the animation
    def init():
        lines[0].set_data([],[])  # empty plot
        return lines
    
    def frame(args):
        frame_no, k, x, fk, taylorsum, lines = args
        #taylorsum+=fk(x,k) #Works some iterations and then crashes
        lines[0].set_data(x, taylorsum[k])
        lines[0].set_label('k=%g' %k)
        plt.legend()
        plt.title("Taylor polynomial evolution")
        plt.savefig('ej5.39Te_%04d.png' % frame_no)
        return lines
    
    all_args = [(frame_no, k, x, fk, taylorsum, lines)
                for frame_no, k in enumerate(klist)]
    
    # Run the animation
    anim = animation.FuncAnimation(
        fig, frame, all_args, interval=150, init_func=init, blit=True)
    
    # Make movie file in MP4 format
    anim.save("ej5.39Te.mp4", fps=4)
    
    ## Make movie files in .gif
    os.system('convert -delay 30 ej5.39Te_*.png ej5.39Te.gif')
    #plt.show()


#!!!!!!!sin(x) fk !!!!!!!!!
#def fk(x,k):
    #return (-1)**k*x**(2*k+1)/(factorial(2*k+1))

#animate_series(fk, 0, 40, 0, 13*np.pi, -2, 2, 235, lambda x: np.sin(x))


#!!!!!!!exp(-x) fk !!!!!!!!!
def fk(x,k):
    return (-x)**k/(factorial(k))

animate_series(fk, 0, 30, 0, 15, -0.25, 1.4, 300, lambda x: np.exp(-x))
