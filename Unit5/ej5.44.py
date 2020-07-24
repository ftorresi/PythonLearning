from math import *
import numpy as np
import matplotlib.pyplot as plt
import sys

_usage=""" Need arguments: f(x), xmin, xmax
Also the number of points along the function curve may be given.
"""

if len(sys.argv)<4:
    raise IndexError(_usage)

form=sys.argv[1]
#Define function
code="""\ndef f(x):
    return %s
    """ %form
exec(code)

try:
    xmin=eval(sys.argv[2])
except NameError:
    print("Second argument xmin must be a real number")
    sys.exit(1)

try:
    xmax=eval(sys.argv[3])
except NameError:
    print("Third argument xmax must be a real number")
    sys.exit(1)
    
    
if len(sys.argv)>4: #get n
    try:
        n=int(sys.argv[4])
    except:
        print(_usage,end="")
        print("Fourth argument must be an integer")
        sys.exit(1)
else:
    n=501


x=np.linspace(xmax,xmin,n)
y=np.zeros_like(x)
#Use a loop since f may be given in math syntax instead of the preferred numpy syntax
try:
    for i in range(len(x)):
        y[i]=f(x[i])
except NameError:
    print('Function must be given between inverted commas, e.g. "sin(x)"')    

plt.plot(x,y,"k-")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x)=%s" %form)
plt.savefig('ej5.44.png')
#plt.show()

