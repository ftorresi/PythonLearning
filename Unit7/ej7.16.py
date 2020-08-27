class Central:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)
        
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)
    
    
def test_Central():
    def f(x):  #Central numerical derivative is exact for cuadratic functions
        return x**2+x-10
    df = Central(f) # Numeric derivative of f
    
    for x in range(100):
        x=0.1*x-2
        der=df(x)
        exact=2*x+1
        tol=1e-8
        assert abs(der-exact)<tol, "Bug in Central"
        
def table(f, v, h=1E-5): #f is a sympy expression
    from sympy import Symbol, diff, lambdify
    x = Symbol('x')
    # make sympy expression
    sympy_dfdx = diff(f, x)
    python_df = lambdify([x], sympy_dfdx)
    python_f= lambdify([x], f)
    d=Central(python_f,h=h)
    
    print("Table of error in central derivative for function %s" %f) 
    print("x         error")
    for x in v:
        err=abs(d(x)-python_df(x))
        print("%-6.2f %10g" %(x,err))


if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        test_Central()
        
        def f(x):
            return 0.25*x**4
        df = Central(f) # make function-like object df
        # df(x) computes the derivative of f(x) approximately
        x = 2
        print ('function: 0.25*x⁴, exact df/dx=x³')
        print ('df(%g)=%g' % (x, df(x)))
        print ('exact:', x**3)
        
        from sympy import Symbol, sin, exp
        x = Symbol('x')
        table(x*exp(x)*sin(x), (0,0.5,1,1.5,2), h=1e-5)
