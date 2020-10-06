
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
    
    
def table(f, xval, methods, dfdx=None): #modified to use values of x instead of h
    # Print headline (x and class names for the methods)
    print ('x',end="    ")
    for method in methods:
        print ('%-15s' % method.__name__,end=" ")
    print ()
    # Print table
    for x in xval:
        print ('%3.1f' %x, end=" ")
        for method in methods:
            if dfdx is not None: # write error
                d = method(f, dfdx_exact=dfdx)
                output = d.error(x)
            else: # write value
                d = method(f)
                output = d(x)
            print ('%15.8E' % output,end=" ")
        print() # newline



if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    
    class v:
        def __init__(self,mu):
            self.mu=mu
            
        def __call__(self,x):
            mu=self.mu
            return ((1-np.exp(x/mu))/(1-np.exp(1.0/mu)))
        
    class derv:
        def __init__(self,mu):
            self.mu=mu
            
        def __call__(self,x):
            mu=self.mu
            return (np.exp(x/mu)/(mu*np.exp(1.0/mu)-mu))
    
    xx=[0.0,0.9]
    methods=[Backward1, Forward1, Forward3, Central2, Central4, Central6]
    
    print("mu=1.0 errors")
    table(v(1.0),xx,methods,derv(1.0))
    
    print("\nmu=0.01 errors")
    table(v(0.01),xx,methods,derv(0.01))
    

    x=np.linspace(0,1,101)
    y1=v(1.0)
    y0=v(0.01)
    plt.figure()
    plt.plot(x,y1(x),label="mu=1")
    plt.plot(x,y0(x),label="mu=0.01")
    plt.legend()
    #plt.show()
    plt.savefig("ej9.8.png")
    
