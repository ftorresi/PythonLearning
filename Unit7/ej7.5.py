import numpy
from math import sqrt

class Cuadratic:
    """Cuadratic function f(x)=a*x**2+b*x+c"""
    
    def __init__(self,a,b,c):
        self.a, self.b, self.c =a, b, c
    
    def value(self,x):
        return self.a*x**2+self.b*x+self.c
    
    def table(self,L=0.,R=1., n=101):
        print("  x           f(x)")
        xlist=numpy.linspace(L,R,n)
        c=Cuadratic(self.a,self.b,self.c)
        for x in xlist:
            print("%-8.3f   %8.3f" %(x, c.value(x)))
        
    def roots(self):
        a, b, c=self.a, self.b, self.c
        d=b**2-4*a*c
        if d==0:
            r=-b/(2*a)
            return r, r
        elif(d>0):
            r1=(-b-sqrt(d))/(2*a)
            r2=(-b+sqrt(d))/(2*a)
            return r1, r2
        else:
            r1=(-b-1j*sqrt(abs(d)))/(2*a)
            r2=(-b+1j*sqrt(abs(d)))/(2*a)
            return r1, r2


def test_Cuadratic():
    c=Cuadratic(1,-3,2) #roots 1 & 2
    x=1.5
    expected_val=x**2-3*x+2
    val=c.value(x)
    tol=1e-10
    assert abs(val-expected_val)<tol, "There's a bug in Cuadratic.value"
    
    exp_r1=1
    exp_r2=2
    r1, r2 = c.roots()
    success=max(abs(r1-exp_r1),abs(r2-exp_r2))<tol
    assert success, "There's a bug in Cuadratic.roots"
    
    print("Output table example")
    c.table(0,20,41)

    
if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        test_Cuadratic()
