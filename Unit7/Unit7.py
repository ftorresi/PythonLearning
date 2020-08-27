### Persons and PhoneBook
#class Person(object):
    #def __init__(self, name,
                 #mobile_phone=None, office_phone=None,
                 #private_phone=None, email=None):
        #self.name = name
        #self.mobile = mobile_phone
        #self.office = office_phone
        #self.private = private_phone
        #self.email = email

    #def add_mobile_phone(self, number):
        #self.mobile = number

    #def add_office_phone(self, number):
        #self.office = number

    #def add_private_phone(self, number):
        #self.private = number

    #def add_email(self, address):
        #self.email = address

    #def __str__(self):
        #s = self.name + '\n'
        #if self.mobile is not None:
            #s += 'mobile phone:   %s\n' % self.mobile
        #if self.office is not None:
            #s += 'office phone:   %s\n' % self.office
        #if self.private is not None:
            #s += 'private phone:  %s\n' % self.private
        #if self.email is not None:
            #s += 'email address:  %s\n' % self.email
        #return s

#class PhoneBook(object):
    #def __init__(self):
        #self.contacts = {}   # dict of Person instances

    #def add(self, name, mobile=None, office=None,
            #private=None, email=None):
        #p = Person(name, mobile, office, private, email)
        #self.contacts[name] = p #key: name, value: person instance w/ person contact info.

    #def __call__(self, name):
        #return self.contacts[name]

    #def __str__(self):
        #s = ''
        #for p in sorted(self.contacts):
            #s += str(self.contacts[p]) + '\n'
        #return s

#def _test():
    #b = PhoneBook()
    #b.add('Ole Olsen', office='767828292',
          #email='olsen@somemail.net')
    #b.add('Hans Hanson',
          #office='767828283', mobile='995320221')
    #b.add('Per Person', mobile='906849781')
    
    #print(type(b))
    #print (b('Per Person')) #calls b.__call__ ("Per Person"), returns its info
    #print (b) #calls b.__str__, returns PhoneBook ordered alphabetically

#if __name__ == '__main__':
    #_test()
    
    
    
### Polynomials    
#import numpy

class Polynomial(object):
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        """Evaluate the polynomial."""
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s

    def __add__(self, other):
        """Return self + other as Polynomial object."""
        # Two cases:
        #
        # self:   X X X X X X X
        # other:  X X X
        #
        # or:
        #
        # self:   X X X X X
        # other:  X X X X X X X X

        # Start with the longest list and add in the other
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]  # copy!
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:] # copy!
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff) #return a Polynomial (not a list of coeff.)

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        #numpy.zeros(M+N+1)
        result_coeff = [0]*(1+N+M) #I prefer a list over an array to be able to use derivative o diferenciate on a product.
        for i in range(0, M+1):
            for j in range(0, N+1):
                result_coeff[i+j] += c[i]*d[j]
        return Polynomial(result_coeff)

    def differentiate(self):
        """Differentiate this polynomial in-place."""
        for i in range(1, len(self.coeff)):
            self.coeff[i-1] = i*self.coeff[i]
        del self.coeff[-1]

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

    def simplestr(self):
        s = ''
        for i in range(0, len(self.coeff)):
            s += ' + %g*x^%d' % (self.coeff[i], i)
        return s


def test_Polynomial():
    p1 = Polynomial([1, -1])
    p2 = Polynomial([0, 1, 0, 0, -6, -1])
    
    p3 = p1 + p2
    p3_exact = Polynomial([1, 0, 0, 0, -6, -1])
    msg = 'p1 = %s, p2 = %s\np3=p1+p2 = %s\nbut wrong p3 = %s'%\
          (p1, p2, p3_exact, p3)
    assert p3.coeff == p3_exact.coeff, msg
    # Note __add__ applies lists only, here with integers, so
    # == for comparing lists is not subject to round-off errors

    p4 = p1*p2
    # p4.coeff becomes a numpy array, see __mul__  ####NOT ANYMORE!
    #p4_exact = Polynomial(numpy.array([0,  1, -1,  0, -6,  5,  1]))
    p4_exact = Polynomial([0,  1, -1,  0, -6,  5,  1])
    msg = 'p1 = %s, p2 = %s\np4=p1*p2 = %s\ngot wrong p4 = %s'%\
          (p1, p2, p4_exact, p4)
    assert p4.coeff == p4_exact.coeff, msg  
    #assert numpy.allclose(p4.coeff, p4_exact.coeff, rtol=1E-14), msg #Check if two arrays are element-wise equal within a tolerance

    p5 = p2.derivative()
    p5_exact = Polynomial([1, 0, 0, -24, -5])
    msg = 'p2 = %s\np5 = p2.derivative() = %s\ngot wrong p5 = %s'%\
          (p2, p5_exact, p5)
    assert p5.coeff == p5_exact.coeff, msg

    p6 = Polynomial([0, 1, 0, 0, -6, -1])  # p2
    p6.differentiate()
    p6_exact = p5_exact
    msg = 'p6 = %s\p6.differentiate() = %s\ngot wrong p6 = %s'%\
          (p2, p6_exact, p6)
    assert p6.coeff == p6_exact.coeff, msg

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'verify':
        test_Polynomial()
