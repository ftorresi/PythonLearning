from math import pi, sin

def S(t,n=10,T=2*pi):
    suma=0.0
    for i in range(1,n+1):
        suma+=(1.0/(2*i-1))*sin(2*(2*i-1)*pi*t/float(T))
    suma*=4/pi
    return suma

def f(t,T=2*pi):
    if 0<t<0.5*T:
        return 1.0
    elif t==0.5*t:
        return 0.0
    elif 0.5*T<t<T:
        return -1.0
    else:
        return "variable value must be lower than %.2f" %T

nlist=(1,3,5,10,30,100)
alphalist=(0.01,0.25,0.49)
values=[[f(alfa*2*pi)-S(alfa*2*pi,m) for alfa in alphalist] for m in nlist] #list whose elements are a list of 3 t/alpha values for fixed n.

print "alpha=    %.2f      %.2f      %.2f" %(alphalist[0],alphalist[1],alphalist[2])

for l in range(len(nlist)):
    print "n=%-3d, %8.5f, %8.5f, %8.5f" %(nlist[l],values[l][0],values[l][1],values[l][2])

print """We se the error decreases with n. It also decreases towards t=T/4 (alpha=0.25) and increases when t is near to the values where the function jumps values (t=0,T/2,T)"""
