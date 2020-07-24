from math import exp
import numpy as np

def f(x):
    return x**3+x*exp(x)+1

v=[2,3,-1]
fv=[]
for n in v:
    fv.append(f(n))

def farray(x):
    return x**3+x*np.exp(x)+1

varray=np.array(v)
fvarray=farray(varray)

for i in range(len(v)):
    if(abs(fv[i]-fvarray[i])<1e-6):
        print("The results are the same for index %g" %i)
