   
### Polynomials    
#import numpy

class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        """Evaluate the polynomial."""
        return sum(self.coeff[power]*x**power for power in self.coeff)
    
    def __add__(self, other):
        """Return self + other as Polynomial object."""
        result = self.coeff.copy()
        for power in other.coeff:
            if power in result:
                result[power]+=other.coeff[power]
            else:
                result[power] = other.coeff[power]
        result_coeff=result.copy()
        for power in result:
            if result[power]==0:
                del result_coeff[power] #delete terms with zero coeff.
        return Polynomial(result_coeff) #return a Polynomial (not a dict of coeff.)  
    
    def __sub__(self, other):
        """Return self - other as Polynomial object."""
        result = self.coeff.copy()
        for power in other.coeff:
            if power in result:
                result[power]-=other.coeff[power]
            else:
                result[power] = -other.coeff[power]
        result_coeff=result.copy()
        for power in result:
            if result[power]==0:
                del result_coeff[power] #delete terms with zero coeff.
        return Polynomial(result_coeff) #return a Polynomial (not a dict of coeff.)   
    
    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        result={}
        for i in c:
            for j in d:
                k=i+j
                if k in result:
                    result[k]+=c[i]*d[j]
                else:
                    result[k]=c[i]*d[j]
        return Polynomial(result)


def test_Polynomial():
    p1 = Polynomial({4: 1, 2: -2, 0: 3})
    p2 = Polynomial({0: 4, 1: 3})
    
    success = (p1(2)-11)<1e-14
    assert success, "Bug in evaluating values"
    success = (p1(-10)-9803)<1e-14
    assert success, "Bug in evaluating values"
    success = (p2(2)-10)<1e-14
    assert success, "Bug in evaluating values"
    success = (p2(-10)+26)<1e-14
    assert success, "Bug in evaluating values"
    
    p3 = p1 + p2
    p3_exact = Polynomial({0: 7, 1: 3,2: -2, 4: 1})
    msg = 'p1 = %s, p2 = %s\np3=p1+p2 = %s\nbut wrong p3 = %s'%(p1, p2, p3_exact, p3)
    assert p3.coeff == p3_exact.coeff, msg
    ## Note __add__ applies lists only, here with integers, so
    ## == for comparing lists is not subject to round-off errors

    p4 = p1*p2
    p4_exact = Polynomial({0: 12, 1: 9, 2: -8, 3: -6, 4: 4, 5: 3})
    msg = 'p1 = %s, p2 = %s\np4=p1*p2 = %s\ngot wrong p4 = %s'%(p1, p2, p4_exact, p4)
    assert p4.coeff == p4_exact.coeff, msg  
    
    p5=p1-p2
    p5_exact = Polynomial({0: -1, 1: -3,2: -2, 4: 1})
    msg = 'p1 = %s, p2 = %s\np5=p1-p2 = %s\nbut wrong p5 = %s'%(p1, p2, p5_exact, p5)
    assert p5.coeff == p5_exact.coeff, msg
    
    p6=p2-p1
    p6_exact = Polynomial({0: 1, 1: 3,2: 2, 4: -1})
    msg = 'p1 = %s, p2 = %s\np6=p2-p1 = %s\nbut wrong p6 = %s'%(p1, p2, p6_exact, p6)
    assert p6.coeff == p6_exact.coeff, msg


if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'verify':
        test_Polynomial()
