""" Making ej3.21 a module"""

from math import pi, sin
import sys
_filename = sys.argv[0]
_usage = """
Usage: %s 2*pi 0.1 0.25 0.49 20 50 100 500]
Program computes the error in the Fourier series for function f(t)={1 if 0<t<T/2; 0 if t=T/2; -1 if T/2<t<T} for given T, a number of 0<alphas<1 so t=alpha*T and the number of terms to use in the Fourier series and prints a table with the  errors for each combination""" % _filename



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

def table(n_values, alpha_values, T):
    values=[[f(alfa*T)-S(alfa*T,m) for alfa in alpha_values] for m in n_values] #list whose elements are a list of error values for different alpha and fixed n.
    
    ncols=len(alpha_values)
    print "alpha = ",
    for i in range(ncols): #print headers
        print "%.2f     " %alpha_values[i],
    print ""
    
    
    for row,n in zip(values,n_values):
        print "n=%-3d " %n,
        for col in row:
            print "%9.5f" %col,
        print ""

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print _usage
    else:
        try:  #read values
            T=float(sys.argv[1])
            alpha=[]
            n=[]
            for i in range(2,len(sys.argv)):
                el=float(sys.argv[i])
                if el<1:
                    alpha.append(el)
                elif el>1:
                    n.append(int(el))
        except:
            print _usage
        
        if T<0: #check for non-negative values
            raise ValueError(_usage)
            sys.exit(1)
        for el in alpha:
            if el<0:
                raise ValueError(_usage)
                sys.exit(1)
                    
        table(n, alpha, T)

