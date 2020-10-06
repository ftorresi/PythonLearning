
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
    
    
def table(f, x, h_values, methods, dfdx=None):
    """
    Write a table of f'(x) computed numerically by
    the methods in the methods list (class names).
    Each row in the table corresponds to a value of
    the discretization parameter h (in h_values).
    If dfdx is not None, dfdx is the exact derivative
    (a function) and the entries in the table are
    the errors in the numerical approximations.
    """
    # Print headline (h and class names for the methods)
    print ('      h       ',end=" ")
    for method in methods:
        print ('%-15s' % method.__name__,end=" ")
    print()  # newline
    # Print table
    for h in h_values:
        print ('%10.2E' % h,end=" ")
        for method in methods:
            if dfdx is not None:
                d = method(f, h, dfdx)
                output = d.error(x)
            else:
                d = method(f, h)
                output = d(x)
            print ('%15.8E' % output,end=" ")
        print()  # newline



if __name__ == '__main__':
    from math import exp

    def f(x):
        return exp(-x)
    
    def F(x):
        return -exp(-x)
    
    xx=0.0
    h_values=[2**-k for k in range(15)]
    methods=[Backward1, Backward2]
    
    table(f,xx,h_values, methods, F)


    
