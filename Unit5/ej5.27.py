import Lagrange_poly2 as lp
import numpy as np
import matplotlib.pyplot as plt

nlist=(2,4,6,10)
plt.figure()
for n in nlist:
    lp.graph(np.abs, n, -2, 2, resolution=1001)
    plt.legend(["n=%d" %n for n in nlist ])
 #plt.savefig("filename.pdf")  if I wanted to save the figure
 
plt.figure()
nlist=(13,20)
for n in nlist:
    lp.graph(np.abs, n, -2, 2, resolution=1001)
    plt.legend(["n=%d" %n for n in nlist ])
plt.show() 
