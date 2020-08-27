class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients
        
    def __call__(self, x):
        return sum([c*x**i for i, c in enumerate(self.coeff)])
    
    def __add__(self, other):
        maxlength = max(len(self.coeff), len(other.coeff))  # BUG in original program, len(self) and len(other) make no sense
        # Extend both lists with zeros to this maxlength
        self.coeff += [0]*(maxlength - len(self.coeff))
        other.coeff += [0]*(maxlength - len(other.coeff))
        result_coeff = self.coeff
        for i in range(maxlength):
            result_coeff[i] += other.coeff[i]
        return Polynomial(result_coeff)
    
#p1 = Polynomial([1, -1])
#p2 = Polynomial([0, 1, 0, 0, -6, -1])
#p3 = p2 + p1
#print (p3.coeff)
