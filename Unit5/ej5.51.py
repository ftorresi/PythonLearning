import numpy as np
import math
import matplotlib.pyplot as plt

def v(x, mu=1E-6, exp=math.exp):
    num=1-exp(x/mu)
    den=1-exp(1./mu)
    v=num/den
    return num, den, v

#m=1E-3
#for i in range(1001):
    #x=0.001*i
    #for e in (math.exp,np.exp):
        #n,d,v=v(x, m, e)
        #print(e, x, n, d, v)
            ###!OUTPUT:
            ###File "ej5.51.py", line 7, in v
            ###den=1-exp(1./mu)
            ###OverflowError: math range error


x=np.linspace(0,1,10001)
n,d,y1=v(x,mu=1,exp=np.exp)
n,d,y2=v(x,mu=0.1,exp=np.exp)
n,d,y3=v(x,mu=0.01,exp=np.exp)
plt.plot(x,y1,"k-", label="mu=1")
plt.plot(x,y2,"r-", label="mu=0.1")
plt.plot(x,y3,"b-", label="mu=0.01") #can't plot 0.001
plt.title("v(x) for various mu")
plt.legend()
plt.savefig("ej5.51vx.png")
plt.show()


m=1E-3
m=np.float96(m)   #AttributeError: module 'numpy' has no attribute 'float96' :(
x2=np.float96(x)  #Can't make it work so I move on.
n,d,y= v(x,mu=m,exp=np.exp)

