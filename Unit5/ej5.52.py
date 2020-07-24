from math import exp
import numpy as np


def farray(x):
    return x**3+x*np.exp(x)+1

A=np.array([[0,2,1],[-1,-1,0],[0,5,0]])

B=farray(A)

C=A**3+A*np.exp(A)+1


check=abs(B-C)<1e-10 #3x3 array with True/False
if check.all()==True:
    print("The two methods are the same.")
else:
    print("The two methods are NOT the same.")
