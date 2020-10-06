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


# A linear function will be exactly integrated by all
# the methods, so such an f is the candidate for testing
# the implementations

def test_Integrate():
    """Check that linear functions are integrated exactly."""
    def f(x):
        return x + 2

    def F(x):
        """Integral of f."""
        return 0.5*x**2 + 2*x

    a = 2; b = 3; n = 4     # test data
    I_exact = F(b) - F(a)
    tol = 1E-15

    methods = [Midpoint, Trapezoidal, Simpson, GaussLegendre2,
               GaussLegendre2_vec]
    for method in methods:
        integrator = method(a, b, n)

        I = integrator.integrate(f)
        assert abs(I_exact - I) < tol

        I_vec = integrator.vectorized_integrate(f)
        assert abs(I_exact - I_vec) < tol
        
def test_MCInt():
    """Test MCInt for 3 points generated with seed, vs results calculated by hand using the same three random numbers"""
    np.random.seed(10)
    #Points: [2.77132064 2.02075195 2.63364823]
    
    def f(x):
        return x + 2
    
    a = 2; b = 3; n = 3     # test data
    mcintegral=MCint(a,b,n)
    MCI_hand = 4.475240275850808 #expected result (not exact)
    tol = 1E-12
    
    I=mcintegral.integrate(f)
    assert abs(MCI_hand - I) < tol
    
    I=mcintegral.vectorized_integrate(f)
    assert abs(MCI_hand - I) < tol
    


import matplotlib.pyplot as plt
from math import log
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

    class F(object):
        def __init__(self, m):
            self.m = float(m)
        def __call__(self, t):
            m = self.m
            return (1 + 1/m)*t**(1/m)

    def exact_integral(a, b, m):
        return b**(1 + 1./m) - a**(1 + 1./m)

    a = 0; b = 1
    n_values = [10, 20, 40, 80, 160, 320, 640]
    for m in 1./4, 1./8., 2, 4, 16:
        f = F(m)
        exact = exact_integral(a, b, m)
        plt.figure()
        for Method in Midpoint, Trapezoidal, Simpson, GaussLegendre2:
            n, e = error_vs_n(f, exact, n_values, Method, a, b)
            plt.plot(n, e, label=Method.__name__)
            plt.legend()
            plt.title('m=%g' % m); plt.xlabel('ln(n)'); plt.ylabel('ln(error)')
        plt.savefig('tmp9.14_%s.png' % m)


def MCI_investigation():
    class F(object):
        def __init__(self, m):
            self.m = float(m)
        def __call__(self, t):
            m = self.m
            return (1 + 1/m)*t**(1/m)

    def exact_integral(a, b, m):
        return b**(1 + 1./m) - a**(1 + 1./m)
    
    a = 0; b = 1
    n_values = [10**k for k in range(3,7)]
    plt.figure()
    for m in 1./4, 1./8., 2, 4, 16:
        f = F(m)
        exact = exact_integral(a, b, m)
        err=[]
        for n_value in n_values:
            integ = MCint(a, b, n_value)
            error = abs(exact - integ.integrate(f))
            err.append(error)
        plt.plot(np.log(n_values), np.log(err),"o-", label="m=%g"%m)
    plt.legend()
    plt.title("MC integration error"); plt.xlabel('ln(n)'); plt.ylabel('ln(error)')
    plt.savefig('ej9.14.png')
        
    

if __name__ == '__main__':
    test_Integrate()
    test_MCInt()
    error_investagation()
    MCI_investigation()
