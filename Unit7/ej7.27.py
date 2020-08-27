   
### Polynomials    
import numpy as np

class Polynomial:
    def __init__(self, coefficients):
        self.coeff = np.asarray(coefficients, dtype=float)

    def __call__(self, x):
        """Evaluate the polynomial."""
        xvec=np.asarray([x**k for k in range(len(self.coeff))])
        return np.dot(self.coeff,xvec) #p(x)=[coeff].[xvec]


    def __add__(self, other):
        """Return self + other as Polynomial object."""
        if len(self.coeff) > len(other.coeff):
            result_coeff=other.coeff+self.coeff[0:len(other.coeff)] #sum the common part
            result_coeff=np.concatenate((result_coeff,self.coeff[len(other.coeff):])) #append the rest of the longest array
        else:
            result_coeff=self.coeff+other.coeff[0:len(self.coeff)] #sum the common part
            result_coeff=np.concatenate((result_coeff,other.coeff[len(self.coeff):])) #append the rest of the longest array
        return Polynomial(result_coeff) #return a Polynomial (not a list of coeff.)
    

    def differentiate(self):
        """Differentiate this polynomial in-place."""
        n = len(self.coeff)
        self.coeff[:-1] = np.linspace(1, n-1, n-1)*self.coeff[1:]
        self.coeff = self.coeff[:-1]

    def derivative(self):
        """Copy this polynomial and return its derivative."""
        dpdx = Polynomial(self.coeff[:])  # make a copy
        dpdx.differentiate()
        return dpdx

    def __str__(self):
        s = ''
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
        # Fix layout
        s = s.replace('+ -', '- ')
        s = s.replace('*x^0', '')
        s = s.replace(' 1*', ' ')
        s = s.replace('x^1 ', 'x ')
        #s = s.replace('x^1', 'x') # will replace x^100 by x^00
        if s[0:3] == ' + ':  # remove initial +
            s = s[3:]
        if s[0:3] == ' - ':  # fix spaces for initial -
            s = '-' + s[3:]
        return s

def test_Polynomial():
    #p.coeff is now a numpy array 
    #numpy.allclose must be used to determine equality
    p1 = Polynomial([1, -1])
    p2 = Polynomial([0, 1, 0, 0, -6, -1])

    p3 = p1+p2
    p3_exact = Polynomial([1, 0, 0, 0, -6, -1])
    msg = 'p1 = %s, p2 = %s\np3=p1+p2 = %s\nbut wrong p3 = %s'%(p1, p2, p3_exact, p3)
    assert np.allclose(p3.coeff, p3_exact.coeff, rtol=1E-14), msg #Check if two arrays are element-wise equal within a tolerance

    p5 = p2.derivative()
    p5_exact = Polynomial([1, 0, 0, -24, -5])
    msg = 'p2 = %s\np5 = p2.derivative() = %s\ngot wrong p5 = %s'% (p2, p5_exact, p5)
    assert np.allclose(p5.coeff, p5_exact.coeff, rtol=1E-14), msg

    p6 = Polynomial([0, 1, 0, 0, -6, -1])  # p2
    p6.differentiate()
    p6_exact = p5_exact
    msg = 'p6 = %s\p6.differentiate() = %s\ngot wrong p6 = %s'%(p2, p6_exact, p6)
    assert np.allclose(p6.coeff, p6_exact.coeff, rtol=1E-14), msg
    

def test_Polynomial_str():
    p=Polynomial([1,-2,-3,1,-1]) #this example has all the "ugly" possibilities
    string="1 - 2*x - 3*x^2 + x^3 - x^4" #expected output
    out=p.__str__()
    success= out==string
    assert success, "Polynomial.__str__ has a bug"
    

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'verify':
        test_Polynomial()
        test_Polynomial_str()
