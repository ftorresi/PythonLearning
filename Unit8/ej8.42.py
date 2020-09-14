def stepstock(x0,mu,sig,T,N):
    dt=T/N
    r=numpy.random.normal(0,1,N)
    x=numpy.zeros(N+1)
    x[0]=x0
    for i in range(1,N+1):
        x[i]=x[i-1]+mu*dt*x[i-1]+sig*x[i-1]*r[i-1]*numpy.sqrt(dt)
    return x


#Main program
import numpy
import matplotlib.pyplot as plt
T=180
N=5000
R=200
avg=0
xm=numpy.zeros(N+1)
for j in range(R):
    xout=stepstock(1,0.0005,0.02,T,N)
    avg+=xout[-1]
    xm+=xout
avg/=R
xm/=R
print("The average stock price after %d days is %g times the initial price"%(T,avg))
time=numpy.linspace(0,T,N+1)
plt.plot(time,xm,"r-")
plt.title("Average price over time")
plt.xlabel("Time [days]")
plt.ylabel("Price normalized to day 0")
plt.axis([-1,T+1,0.95*numpy.min(xm),1.02*numpy.max(xm)])
plt.savefig("ej8.42.png")
#plt.show()
