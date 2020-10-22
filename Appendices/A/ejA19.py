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
    tag='y0=%3.1f, q=%g, N=%i' %(y0,q,N)
    plt.plot(index,y,label=tag)
    plt.legend()
    plt.xlabel('Time Units')
    plt.ylabel('Normalized number of individuals')
    plt.savefig('ejA19.png')
    #plt.show()


if __name__ == '__main__':
    try:
        y0=float(sys.argv[1])
        q=float(sys.argv[2])
        N=int(sys.argv[3])
    except IndexError:
        print ('Usage: %s y0 q N' % sys.argv[0])
        sys.exit(1)

    logistic(y0,q,N)
    
