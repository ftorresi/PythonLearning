from math import pi
import numpy as np
import matplotlib.pyplot as plt

#Vectorized W-like function
def w(x,T=2): #function defined in [-T,T]
    condition1=abs(x)<=0.5*T
    condition2=np.logical_and(abs(x)>0.5*T, abs(x)<=T)
    
    r=np.zeros_like(x)
    r[condition1]=1-2.0*abs(x[condition1])/T
    r[condition2]=2.0*abs(x[condition2])/T-1
    return r

   
T0=2
x=np.linspace(-T0,T0,int(100*T0+1))
y=w(x,T0)

plt.plot(x,y,"k-")
plt.xlabel("x")
plt.ylabel("W(x)")
plt.title("W-shaped function ")
plt.savefig('ej5.46.png')
#plt.show()

def test_w():
    Tlist=np.linspace(0.1,100,40)
    expect=np.array([1,0.5,0,0.5,1,.5,0,0.5,1]) #expected values in testing points
    for T0 in Tlist:
        xlist=np.linspace(-T0,T0,9) #points spaced T0/4
        ylist=w(xlist,T0)
        check=((ylist-expect)<1e-10) #array of 9 True or False values
        msg="error in checking point for T0=%g" %T0
        assert check.all(), msg #verify that ALL values in check are True

#test_w()
        
