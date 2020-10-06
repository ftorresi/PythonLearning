import numpy as np
import math

class Integrator(object):
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



#import matplotlib.pyplot as plt
from math import log, sin, exp, cos
def error_investagation():

    def error_vs_n(f, exact, n_values, Method, a, b):
        """
        Compute errors in numerical integration of f from a
        to b with Method, using a range of n values (n_values).
        Return actual n values and errors as two lists.
        """
        log_n = []  # log of actual n values (Method may adjust n)
        log_e = []  # log of corresponding errors
        for n_value in n_values:
            method = Method(a, b, n_value)
            error = abs(exact - method.integrate(f))
            log_n.append(log(method.n))
            log_e.append(log(error))
        return log_n, log_e
    
    def f(x):
        return 2*x*sin(x)+x**2*cos(x)+5*x**4
    
    def F(x):
        return x**2*sin(x)+x**5
    
    def exact_integral(a, b):
        return F(b)-F(a)

    a = 0; b = 2
    n_values = [2**k+1 for k in range(2,12)]
    exact = exact_integral(a, b)
    for Method in Midpoint, Trapezoidal, Simpson, GaussLegendre2:
            n, e = error_vs_n(f, exact, n_values, Method, a, b)
            print("Method:%s, Error estimated as E=C*n**r" %Method.__name__)
            for i in range(len(n)-1):
                r=(e[i]-e[1+i])/(n[i]-n[i+1]) #note that e and n are ln of error and nvalues, respectively
                C=exp(e[1+i]-r*n[1+i])
                N=int(exp(n[i+1]))
                print("n=%g r=%g, C=%g"%(N,r,C))
            

if __name__ == '__main__':
    error_investagation()

