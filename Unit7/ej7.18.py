class DerivativeP:
    
    def __init__(self, f, h=1E-5):
        self._f = f
        self._h = float(h)
        
    def __call__(self, x):
        f, h = self._f, self._h
        return (f(x+h) - f(x))/h
    
    def get_precision(self):
        return self._h
        
    def set_precision(self, h):
        self._h=float(h)
        
        
def test_DerivativeP():
    # The formula is exact for linear functions, regardless of h
    f = lambda x: a*x + b
    a = 3.5; b = 8
    dfdx = DerivativeP(f, h=0.5)
    diff = abs(dfdx(4.5) - a)
    assert diff < 1E-13, 'bug in class DerivativeP, diff=%s' % diff
    hh=0.1
    dfdx.set_precision(hh)
    diff = abs(dfdx(4.5) - a)
    assert diff < 1E-13, 'bug in DerivativeP.set_precision, diff=%s' % diff
    h3=dfdx.get_precision()
    assert abs(hh-h3)<1E-13, 'bug in DerivativeP.get_precision'
    

test_DerivativeP()
