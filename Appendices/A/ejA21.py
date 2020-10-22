import sys
import numpy as np
import matplotlib.pyplot as plt

def logistic(y0,q,N):
    index=np.arange(N+1)
    y=np.zeros(N+1)
    y[0]=y0
    for i in index[1:]:
        y[i]=y[i-1]+q*y[i-1]*(1-y[i-1])
    plt.figure()
    tag='y0=%4.2f, q=%g' %(y0,q)
    plt.plot(index,y)
    plt.title(tag)
    plt.xlabel('Time Units')
    plt.ylabel('Normalized number of individuals')
    filename='ejA20-%4.2f-%3.1f-%i.png' %(y0,q,N)
    plt.savefig(filename)
    return filename
    #plt.show()


if __name__ == '__main__':
       
    N=50
    qlist=[0.1,1,1.5,1.8,2,2.5,3]
    y0list=[0.01,0.3]
    
    outfile=open("ejA21-report.html","w")
    outfile.write("<html> \n")
    outfile.write("<body> \n")
    
    for y0 in y0list:
        for q in qlist:
            name=logistic(y0,q,N)
            outfile.write('<p><img src="%s"> \n' %name)
            
    outfile.write("</html> \n")
    outfile.write("</body>")
    outfile.close()
