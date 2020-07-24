import numpy as np
import matplotlib.pyplot as plt
import sys
#NOTE: Output example made with options: "np.sin(x)*np.exp(x)" 0 4 401 "ej5.15.out"
try:
    func=sys.argv[1]
    a=float(sys.argv[2])
    b=float(sys.argv[3])
    n=int(sys.argv[4])
    outname=sys.argv[5]
except IndexError:
    print("Need arguments f, a, b, n, output file name")
    sys.exit(1)

outfile=open(outname,"w")
fdef = """
def f(x):
   return %s
""" %func
exec(fdef)

x=np.linspace(a, b, n)
y=f(x)

for i in range(x.size):
    outfile.write("%7.3f %7.3f \n" %(x[i], y[i]))

outfile.close()
