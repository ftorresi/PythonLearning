import numpy as np

class Integral_eff:
    def __init__(self, f, a, n=100):
        self.f, self.a, self.n = f, a, n
        
    def __call__(self, x):
        x=np.asarray(x)
        f=np.zeros_like(x)
        f[0]=0
        mi=int((x[0]-self.a)*self.n/(x[-1]-self.a))
        if mi>=1:  #if x[0]!=a
            f[0]=self.trapezoidal(self.a, x[0], mi)
        for i in range(1,len(x)):
             mi=int((x[i]-x[i-1])*self.n/(x[-1]-self.a))
             f[i]=f[i-1]+self.trapezoidal(x[i-1], x[i], mi)
        return f

    
    def trapezoidal(self, xi, xf, m):
        f=self.f
        h = (xf-xi)/float(m)
        I = 0.5*(f(xi)+f(xf))
        for i in range(1, m):
            I += f(xi + i*h)
        I *= h
        return I
    


def test_Integral_eff():
    def g_test(t):
        """Linear integrand."""
        return 2*t + 1
    
    def f_test(x, a):  #f=integral(g)
        """Exact integral of g_test."""
        return x**2 + x - (a**2 + a)
    
    a = 2
    I=Integral_eff(g_test,a,1000)
    x=np.linspace(2,10,33)
    f=I(x)
    f_exact = f_test(x, a)
    assert np.allclose(f_exact, f), "bug in class Integral_eff"
    

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        test_Integral_eff()
        print("Test OK")
    
