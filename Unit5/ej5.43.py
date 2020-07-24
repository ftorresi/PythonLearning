from math import *
import numpy as np
import matplotlib.pyplot as plt
import sys

form=sys.argv[1]
xmin=eval(sys.argv[2])
xmax=eval(sys.argv[3])

#Define function
code=""" 
def f(x):
    return %s
""" %form
exec(code)

x=np.linspace(xmax,xmin,501)
y=np.zeros_like(x)
#Use a loop since f may be given in math syntax instead of the preferred numpy syntax
for i in range(len(x)):
    y[i]=f(x[i])
    

plt.plot(x,y,"k-")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x)=%s" %form)
plt.savefig('ej5.43.png')
#plt.show()

