import numpy as np
import matplotlib.pyplot as plt
import sys


def readdata():
    try:
        inname=sys.argv[1]
    except IndexError:
        print("Need input file nameas argument")
        sys.exit(1)
    
    infile=open(inname,"r")
    

    infile.readline()  #skip first line
        
    x=[]
    y=[]
    for line in infile:
        data=line.split()
        x.append((data[0]))
        y.append((data[1]))
        
    infile.close()
    
    #transform to float
    for i in range(len(x)):
        x[i]=float(x[i])
        y[i]=float(y[i])
    #
    return x, y


def expected(x):
    return 2*np.pi*np.sqrt(x/9.81) #theoretical expected fit


def fit(x, y, deg=[1]):
    plt.figure()
    plt.plot(x,y, "o",label='data')
    xmin=np.min(x)
    xmax=np.max(x)
    xpol=np.linspace(xmin, xmax, 100)
    for d in deg:
        coeff = np.polyfit(x, y, d)
        p = np.poly1d(coeff)
        print("for degree %d the fitting formula is: \n %s" %(d,p)) #print ecuations
        ypol=p(xpol)
        plt.plot(xpol, ypol, "-.",label='fitted polynomial of degree %d' %d)
    ytheor=expected(xpol)
    plt.plot(xpol, ytheor, "k-",label='theoretical relation T=2pi*sqrt(L/g)')
    plt.legend()
    plt.xlabel("L [m]")
    plt.ylabel("T [s]")
    plt.title("Data fitted to polynomials")
    plt.show()
        
x, y=readdata() 
#transform data to arrays
x=np.array(x)
y=np.array(y)

#call fit
deg=[1,2,3]
fit(x, y, deg)
