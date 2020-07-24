from math import factorial
import numpy as np
import matplotlib.pyplot as plt

def S(x, n):
    s=0.0
    for j in range(n+1):
        s+=(-1.)**j*x**(2.*j+1)/float(factorial(2*j+1))
    return s

x=np.linspace(0,4*np.pi,2001)
y=np.sin(x)
y1=S(x,1)
y2=S(x,2)
y3=S(x,3)
y6=S(x,6)
y12=S(x,12)

plt.figure()
plt.plot(x, y, "-",label="sin x")
plt.plot(x, y1, "-.",label="S(x,1)")
plt.plot(x, y2, "-.",label="S(x,2)")
plt.plot(x, y3, "-.",label="S(x,3)")
plt.plot(x, y6, "-.",label="S(x,6)")
plt.plot(x, y12, "-.",label="S(x,12)")
plt.axis([0, 13, -5, 5])
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin x and Taylor approximations")
plt.show()


