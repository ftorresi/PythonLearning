with open("ej6.15.html","w") as outfile:
    outfile.write("<html><body><h1>")
    outfile.write("Code to solve Exercise 5.33  </h1> \n")
    outfile.write("<hr> \n")
    outfile.write("<pre> \n")
    outfile.write("import numpy as np \n")
    outfile.write("import matplotlib.pyplot as plt\n")
    outfile.write("import matplotlib.animation as animation\n")
    outfile.write("import time, glob, os\n \n")
    outfile.write("def f(x,t=0):\n")
    outfile.write("    return np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))\n \n")
    outfile.write("x=np.linspace(-6,6,1001) \n")
    outfile.write("tmax=1.0 \n")
    outfile.write("tmin=-1.0 \n")
    outfile.write("tlist=np.linspace(tmin,tmax,61) \n \n")
    outfile.write("#Clean up old frames\n")
    outfile.write("for name in glob.glob('wp_*.png'):\n")
    outfile.write("   os.remove(name)\n \n")
    outfile.write("# Make a first plot (save the lines objects returned from plt.plot)\n")
    outfile.write("fig = plt.figure() \n")
    outfile.write("plt.axis([x[0], x[-1], -1.05, 1.05]) \n")
    outfile.write("lines = plt.plot([],[]) \n")
    outfile.write("plt.xlabel('x') \n")
    outfile.write("plt.ylabel('f(x,t)') \n \n")
    outfile.write("# Function to return the background plot in the animation \n")
    outfile.write("def init(): \n")
    outfile.write("   lines[0].set_data([], [])  # empty plot \n")
    outfile.write("   return lines \n \n")    
    outfile.write("# Function to return a frame in the movie \n")        
    outfile.write("def frame(args): \n")       
    outfile.write("    frame_no, t, x, lines = args \n")     
    outfile.write("    y = f(x, t) \n")     
    outfile.write("    lines[0].set_data(x, y) \n")     
    outfile.write("    lines[0].set_label('t=%4.2f' %t) \n")    
    outfile.write("    plt.legend() \n")     
    outfile.write("    plt.savefig('wp_%04d.png' % frame_no) \n")    
    outfile.write("    return lines \n \n")     
    outfile.write("# Construct list of all arguments to frame function \n")   
    outfile.write("# (each call sends frame number, t value, x array, and lines list) \n")    
    outfile.write("all_args = [(frame_no, t, x, lines) \n")    
    outfile.write("           for frame_no, t in enumerate(tlist)]\n  \n")  
    outfile.write("# Run the animation \n")    
    outfile.write("anim = animation.FuncAnimation( \n")    
    outfile.write("   fig, frame, all_args, interval=150, init_func=init, blit=True) \n \n")    
    outfile.write("# Make movie file in .gif format \n")  
    outfile.write(" os.system('convert -delay 30 wp_*.png ej5.33wp.gif') \n")
    outfile.write("</pre> \n")
    outfile.write("<hr> \n")
    outfile.write("<h2>Some example output images  </h2> \n")   
    outfile.write("<img src='ej6.15-1.png'>\n") 
    outfile.write("<img src='ej6.15-2.png'>\n") 
    outfile.write("<img src='ej6.15-3.png'>\n") 
    outfile.write("<hr> \n")
    outfile.write("<h2>Movie (.gif) obtained as output </h2> \n")   
    outfile.write("<img src='ej15wp.gif'>\n") 
    outfile.write("</body></html>")






















