from math import exp, cos, log, pi

def diff(f, x, h=1E-5):
    der=(f(x+h)-f(x-h))/(2.0*h)
    return der

a=2; b=-3; c=7
def cuad(x): #cuadratic function to test diff
    global a, b, c
    return a*x**2+b*x+c

def test_diff():
    x0=11
    global a, b, c
    expected=2*a*x0+b
    val=diff(cuad, x0, h=1E-2)
    success=abs(expected-val)<1e-10
    msg="test fails for cuadratic function"
    assert success, msg
    
test_diff()


### Part c
def gauss(x):
    return exp(-2*x**2)


def application():
    print "x      function   f'(x)    error"
    funcs=[exp,gauss,cos,log]
    xval=[0,0,2*pi,1]
    expect=(1,0,0,1) # expected values
    results=[]
    for f,x in zip(funcs,xval):
        val=diff(f, x, h=1E-2)
        results.append(val)
    for f,x,der,res in zip(funcs,xval, expect, results):
        print "%.5f, %-5s, %.6f, %.6f" %(x,f.__name__,res,abs(res-der))
        
application()
    
    #dex=diff(exp, 0, h=1E-2)
    #dgauss=diff(gauss, 0, h=1E-2)
    #dcos=diff(cos, 2*pi, h=1E-2)
    #dlog=diff(log, 1, h=1E-2)
    
