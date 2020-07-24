from math import pi, exp, sqrt

def h(x):
    return exp(-0.5*x**2)/sqrt(2*pi)

n=41
dx=8./(n-1)
xlist=[-4+dx*i for i in range(n)]
hlist=[h(x) for x in xlist]

for i in range(n):
    print xlist[i], hlist[i]
