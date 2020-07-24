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
    
    for i in range(4): #skip 4 lines
        infile.readline()
        
    x=[]
    y=[]
    for line in infile:
        data=line.split()
        x.append((data[0]))
        y.append((data[1]))
        
    infile.close()
    
    del x[-1] #remove last item
    del y[-1] #remove last item
    
    #transform to float
    for i in range(len(x)):
        x[i]=float(x[i])
        y[i]=float(y[i])
    #
    return x, y


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
    plt.legend()
    plt.xlabel("T[°C]")
    plt.ylabel("density [kg/m^3]")
    plt.title("Data fitted to polynomials")
    plt.show()
        

x, y=readdata() 
#transform data to arrays
x=np.array(x)
y=np.array(y)

#call fit
deg=[1,2]
fit(x, y, deg)
