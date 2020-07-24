import numpy as np
import matplotlib.pyplot as plt

def trapezint(f, a, b, n):
  h=float(b-a)/n
  data=np.zeros((n+1,2))
  data[0][0]=a
  data[0][1]=f(a)
  data[-1][0]=b
  data[-1][1]=f(b)
  integral=0.5*h*(data[0][1]+data[-1][1])
  for i in range(1,n):
    data[i][0]=a+i*h
    data[i][1]=f(data[i][0])
    integral+=h*data[i][1]
  return integral, data


def linsteps(x, data): #data=[{(xi,vi)}] #straight lines joining data points
    x=np.asarray(x)
    err=np.logical_and(x>=data[0][0],x<=data[-1][0]) #boolean array, same len as x, check all values are greater than the minimum and smaller than the maximum
    if not err.all(): #if err aren't all True:
        print (" All arguments must be greater than or equal to %.2f and smaller than or equal to %.2f" %(data[0][0],data[-1][0]) )
        return None
    r=np.zeros_like(x)
    for i in range(len(data)-1):
        condition=np.logical_and(x>=data[i][0],x<data[i+1][0])
        r[condition]=(x[condition]*(data[i+1][1]-data[i][1])-data[i+1][1]*data[i][0]+data[i+1][0]*data[i][1])/(data[i+1][0]-data[i][0])
    r[-1]=data[-1][1]
    return r
        
def vlines(x,data):
    r=np.zeros_like(x)
    h=(x[-1]-x[0])/float(len(x)-1)
    for i in range(len(data)):
        condition=abs(x-data[i][0])<=0.5*h
        r[condition]=data[i][1]
    r[-1]=data[-1][1]
    return r


def plot_trapezint(f, a, b, n):
    x=np.linspace(a,b,int(100.0*(b-a))) #plot 100 points per x-unity
    y1=f(x)
    integral, data= trapezint(f, a, b, n)
    y2=linsteps(x, data)
    y3=vlines(x,data)
    
    plt.plot(x,y1,"r-")
    plt.plot(x,y2,"r--")
    plt.plot(x,y3,"r:")
    plt.fill_between(x,y1,y2)
    plt.axis([a,b,min(np.min(y1),np.min(y2)),1.02*max(np.max(y1),np.max(y2))])
    plt.title("Trapezoidal rule illustration")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig('ej5.50tr.png')
    plt.show()
    

def f(x):
    return (12-x)*x+np.sin(np.pi*x)

a=0
b=10
n=7
plot_trapezint(f, a, b, n)
