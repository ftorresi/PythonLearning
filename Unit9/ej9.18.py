import numpy as np
import matplotlib.pyplot as plt
#Copy classes for differentiate, integrate and extrema. In a real situation, they should be imported

#-------class for differentiation----------
class Diff2:
    def __init__(self, f, h=1E-5, dfdx_exact=None):
        self.f = f
        self.h = float(h)
        self.exact = dfdx_exact

    def error(self, x):
        if self.exact is not None:
            df_numerical = self(x)
            df_exact = self.exact(x)
            return df_exact - df_numerical

class Forward1(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h

class Backward1(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h

class Central2(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)

class Central4(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (4./3)*(f(x+h)   - f(x-h))  /(2*h) - \
               (1./3)*(f(x+2*h) - f(x-2*h))/(4*h)

class Central6(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (3./2) *(f(x+h)   - f(x-h))  /(2*h) - \
               (3./5) *(f(x+2*h) - f(x-2*h))/(4*h) + \
               (1./10)*(f(x+3*h) - f(x-3*h))/(6*h)

class Forward3(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (-(1./6)*f(x+2*h) + f(x+h) - 0.5*f(x) - \
                (1./3)*f(x-h))/h
    
class Backward2(Diff2):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x-2*h)-4*f(x-h)+3*f(x))/(2*h)
#--------------------------------------------------------------

#----------------class for integration------------------
class Integrator:
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.construct_method()

    def construct_method(self):
        raise NotImplementedError('no rule in class %s' %
                                  self.__class__.__name__)

    def integrate(self, f):
        s = 0
        for i in range(len(self.weights)):
            s += self.weights[i]*f(self.points[i])
        return s

    def vectorized_integrate(self, f):
        return np.dot(self.weights, f(self.points))
    
class MCint(Integrator):
    def construct_method(self):
        x=np.random.uniform(self.a,self.b,self.n)
        h = (self.b-self.a)/float(self.n)
        w = np.zeros(len(x)) + h
        return x, w


class Midpoint(Integrator):
    def construct_method(self):
        a, b, n = self.a, self.b, self.n  # quick forms
        h = (b-a)/float(n)
        x = np.linspace(a + 0.5*h, b - 0.5*h, n)
        w = np.zeros(len(x)) + h
        return x, w

class Trapezoidal(Integrator):
    def construct_method(self):
        x = np.linspace(self.a, self.b, self.n)
        h = (self.b - self.a)/float(self.n - 1)
        w = np.zeros(len(x)) + h
        w[0] /= 2
        w[-1] /= 2
        return x, w

class Simpson(Integrator):
    def construct_method(self):
        if self.n % 2 != 1:
            print ('n=%d must be odd, 1 is added' % self.n)
            self.n += 1
        x = np.linspace(self.a, self.b, self.n)
        h = (self.b - self.a)/float(self.n - 1)*2
        w = np.zeros(len(x))
        w[0:self.n:2] = h*1.0/3
        w[1:self.n-1:2] = h*2.0/3
        w[0] /= 2
        w[-1] /= 2
        return x, w

class GaussLegendre2(Integrator):
    def construct_method(self):
        if self.n % 2 != 0:
            print ('n=%d must be even, 1 is subtracted' % self.n)
            self.n -= 1
        nintervals = int(self.n/2.0)
        h = (self.b - self.a)/float(nintervals)
        x = np.zeros(self.n)
        sqrt3 = 1.0/math.sqrt(3)
        for i in range(nintervals):
            x[2*i]   = self.a + (i+0.5)*h - 0.5*sqrt3*h
            x[2*i+1] = self.a + (i+0.5)*h + 0.5*sqrt3*h
        w = np.zeros(len(x)) + h/2.0
        return x, w

class GaussLegendre2_vec(Integrator):
    def construct_method(self):
        if self.n % 2 != 0:
            print ('n=%d must be even, 1 is added' % self.n)
            self.n += 1
        nintervals = int(self.n/2.0)
        h = (self.b - self.a)/float(nintervals)
        x = np.zeros(self.n)
        sqrt3 = 1.0/math.sqrt(3)
        m = np.linspace(0.5*h, (nintervals-1+0.5)*h, nintervals)
        x[0:self.n-1:2] = m + self.a - 0.5*sqrt3*h
        x[1:self.n:2]   = m + self.a + 0.5*sqrt3*h
        w = np.zeros(len(x)) + h/2.0
        return x, w
#--------------------------------------------------------------

#----------------class for function extrema------------------    
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
#--------------------------------------------------------------



class CalculusCalculator:
    def __init__(self, f, a, b, resolution=101):
        self.f, self.a, self.b =f, a, b
        self.res=resolution
        self.x=np.linspace(a,b,resolution)
        self.diffmethod=Central2  #default differentiation method
        self.intmethod=Trapezoidal #default integration method
        try:
            self.y=self.f(x)
        except: #in case f is not array-friendly
            self.y=[]
            for xval in self.x:
                self.y.append(f(xval))
        
    def plot(self,style="ro-",tag="function"): #later can add more option: axis label, legend, title...
        plt.plot(self.x,self.y,style,label=tag)
        plt.legend()
        
    def plot_derivative(self,style="bo.-",tag="derivative"): #later can add more option: axis label, legend, title...
        diff=self.diffmethod(self.f)
        dy=[]
        for xv in self.x:    #make list for f'(x)
            dy.append(diff(xv))
        plt.plot(self.x,dy,style,label=tag)
        plt.legend()
    
    def extreme_points(self):
        mm=MinMax(self.f,self.a, self.b, self.res)
        print()
        print(mm)
        print()
    
    
    def set_differentiation_method(self,method):
        self.diffmethod=method
        
    def df(self,x):
        method=self.diffmethod
        derivate=method(self.f)
        return derivate(x)    
    
    
    def set_integration_method(self,method):
        self.intmethod=method
        
    def integral(self):
        method=self.intmethod
        integral=method(self.a,self.b,self.res)
        return integral.integrate(self.f)
    
        
    
    
def f(x):
    return x**2*np.exp(-0.2*x)*np.sin(2*np.pi*x)

c = CalculusCalculator(f, 0, 6, resolution=700)
plt.figure()
c.plot("b-") # plot f
c.plot_derivative("k-.") # plot f'
c.extreme_points()



print(c.df(2.51))
c.set_differentiation_method(Central4)
print(c.df(2.51))

print(c.integral())
c.set_integration_method(Simpson) # more accurate integration
print(c.integral())

plt.show()


