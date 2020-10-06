class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients
        
    def __call__(self, x):
        """Evaluate the polynomial."""
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s



class Parabola(Polynomial):
    def __init__(self, c0, c1, c2):
        coeff=[c0, c1, c2] #coefficients for Polynmial must be in a list
        Polynomial.__init__(self, coeff) 
    
    def __call__(self, x):
        return Polynomial.__call__(self, x)
    

class Line(Parabola):
    def __init__(self, c0, c1):
        Parabola.__init__(self, c0, c1, 0)


l=Line(1,2)
p=Parabola(1,2,1)

print(l(1))
print(l(-1/2))
print(p(1))
print(p(-1))

    
