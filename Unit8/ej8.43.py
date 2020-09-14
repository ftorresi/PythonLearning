def stock(s0,r,sig,T):
    "Stock value dynamics from day 0 to T"
    eps=numpy.random.normal(0,1,T)
    s=numpy.zeros(T+1)
    s[0]=s0
    for i in range(1,T+1):
        s[i]=(1+r)*s[i-1]+sig*s[i-1]*eps[i-1]
    return s

def avg_stock(s):
    "Average Stock Value"
    avg=(numpy.sum(s))/len(s)
    return avg

def price(s0,r,sig,T,K,N=1000):
    "Price of Asian Option"
    priceevo=[]
    ep=0
    for i in range(N):
        st=stock(s0,r,sig,T)
        avg_st=avg_stock(st)
        ep+=max((avg_st-K),0)/(1+r)**T
        priceevo.append(ep/(i+1))
    return priceevo

def plotprice(p):
    nval=numpy.arange(1,1+len(p))
    pfinal=numpy.full(len(p),p[-1],dtype=float)
    plt.figure()
    plt.plot(nval,p,"r-",label="Price over simulations")
    plt.plot(nval,pfinal,"b:",label="Final price")
    plt.legend()
    plt.axis([-0.02*nval[-1],1.02*nval[-1],0.9*min(p),1.05*max(p)])
    plt.xlabel("Number of simulations")
    plt.ylabel("Option Price")
    plt.savefig("ej8.43price.png")
    
def ploterror(p):
    nval=numpy.arange(1,1+len(p))
    p=numpy.asarray(p)
    p=numpy.abs(p-p[-1]) #error array
    plt.figure()
    plt.plot(nval,p,"r-",label="Error")
    plt.axis([-0.02*nval[-1],1.02*nval[-1],0.9*min(p),1.05*max(p)])
    plt.xlabel("Number of simulations")
    plt.ylabel("Error in price")
    #Error fitting 
    sq=p[0]/numpy.sqrt(nval)
    plt.plot(nval,sq,"b-.",label="~1/sqrt(N)")
    plt.legend()
    plt.savefig("ej8.43error.png")

#Main program
import numpy
import matplotlib.pyplot as plt
pN=price(100,0.0002,0.015,100,102,10000)
print("The estimated price for the Options is %10.8f"%pN[-1])
plotprice(pN)
ploterror(pN)


#import matplotlib.pyplot as plt
#T=180
#N=5000
#R=200
#avg=0
#xm=numpy.zeros(N+1)
#for j in range(R):
    #xout=stepstock(1,0.0005,0.02,T,N)
    #avg+=xout[-1]
    #xm+=xout
#avg/=R
#xm/=R
#print("The average stock price after %d days is %g times the initial price"%(T,avg))
#time=numpy.linspace(0,T,N+1)
#plt.plot(time,xm,"r-")
#plt.title("Average price over time")
#plt.xlabel("Time [days]")
#plt.ylabel("Price normalized to day 0")
#plt.axis([-1,T+1,0.95*numpy.min(xm),1.02*numpy.max(xm)])
#plt.savefig("ej8.42.png")
##plt.show()
