class MinMax:
    def __init__(self, f, a, b, n):
        self.f, self.a, self.b, self.n=f,a,b,n
        self._find_extrema()
        
    def _find_extrema(self):
        f,a,b,n=self.f, self.a, self.b, self.n
        pmin, pmax, fmin, fmax=[], [], [], []
        h=(b-a)/float(n)
        x0=a
        x1=a+h
        f0=f(x0)
        f1=f(x1)
        if (f0<f1):
            pmin.append(x0)
            fmin.append(f0)
        else:
            pmax.append(x0)
            fmax.append(f0)
        for i in range(1,n): #evaluate from a+h to a+(n-1)h=b-h
            x2=x1+h
            f2=f(x2)
            if (f0>f1 and f1<f2): #local min
                pmin.append(x1)
                fmin.append(f1)
            elif (f0<f1 and f1>f2): #local max
                pmax.append(x1)
                fmax.append(f1)
            x0=x1   #prepare to evaluate next point
            f0=f1
            x1=x2
            f1=f2
        if (f1<f0): #at the end of the loop, x1=b and x0=b-h
            pmin.append(x1)
            fmin.append(f1)
        else:
            pmax.append(x1)
            fmax.append(f1)
        self.pmax, self.pmin, self.fmax, self.fmin=pmax, pmin, fmax, fmin
        self.fmaxglob=max(fmax)
        self.fminglob=min(fmin)
        self.pmaxglob=pmax[fmax.index(self.fmaxglob)]
        self.pminglob=pmin[fmin.index(self.fminglob)]
        
    def get_global_minimum(self):
        return self.pminglob, self.fminglob
    
    def get_global_maximum(self):
        return self.pmaxglob, self.fmaxglob
    
    def get_all_minima(self):
        return [(self.pmin[i], self.fmin[i]) for i in range(len(self.pmin))]
    
    def get_all_maxima(self):
        return [(self.pmax[i], self.fmax[i]) for i in range(len(self.pmax))]
    
    def __str__(self):
        s="All minima: "
        for m in self.pmin:
            s+="%g, " %m
        s=s[:-2] #eliminate last comma
        s+="\nAll maxima: "
        for m in self.pmax:
            s+="%g, " %m
        s=s[:-2] #eliminate last comma
        s+="\nGlobal minimum: %g" %self.pminglob
        s+="\nGlobal maximum: %g" %self.pmaxglob  
        return s

from math import exp, sin, pi
def f(x):
    return x**2*exp(-0.2*x)*sin(2*pi*x)
m = MinMax(f, 0, 4, 5000)
print (m)
#print(m.get_global_maximum())
#print(m.get_global_minimum())
#print(m.get_all_maxima())
#print(m.get_all_minima())
