import numpy as np
import math

class Integrator(object):
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.construct_method()

    def construct_method(self):
        raise NotImplementedError('no rule in class %s' %
                                  self.__class__.__name__)
    
    def __call__(self, func, x):
        x=np.asarray(x)
        f=np.zeros_like(x)
        f[0]=0
        n0=self.n #Total n, not to be overwritten by mi in self.__init__
        a0=self.a #Starting a, not to be overwritten by mi in self.__init__
        mi=int((x[0]-a0)*n0/(x[-1]-a0))
        if mi>=1:  #if x[0]!=a
            self.__init__(a0, x[0], mi)
            f[0]=self.integrate(self,func)
        for i in range(1,len(x)):
             mi=int((x[i]-x[i-1])*n0/(x[-1]-a0))
             self.__init__(x[i-1], x[i], mi)
             f[i]=f[i-1]+self.integrate(func)
        return f

    def integrate(self, f):
        s = 0
        for i in range(len(self.weights)):
            s += self.weights[i]*f(self.points[i])
        return s

    def vectorized_integrate(self, f):
        return np.dot(self.weights, f(self.points))


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
        return 2*x -3

    def F(x):
        """Integral of f."""
        return x**2 -3*x

    a = 0; b = 10; n = 400   
    xx=np.asarray([0.5*i for i in range(21)])

    methods = [Midpoint, Trapezoidal, Simpson, GaussLegendre2,
               GaussLegendre2_vec]
    for method in methods:
        integrator = method(a, b, n) #Select method, starting point a and n. b is irrelevant in this case
        output=integrator(f,xx)  #give function and array of points xx as input, output is an array with integral values for xx
        exact=F(xx) #exact value
        assert np.allclose(exact,output) #check if both arrays are close within tolerance
        


if __name__ == '__main__':
    test_Integrate()
