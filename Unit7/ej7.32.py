
class IntervalMath(object):
    """
    Class for computing with quantities specified by intervals
    (in which the true value of the quantity is guaranteed to lie).
    """
    def __init__(self, lower, upper):
        """Create interval from lower and upper limits."""
        if lower <= upper:
            self.lo = float(lower)
            self.up = float(upper)
        else:
            raise ValueError\
                  ('lower limit %s must be smaller than upper limit %s' %
                   (lower, upper))

    @staticmethod
    def n2i(n):
        """Turn number or interval n into interval."""
        if isinstance(n, (int, float)):
            return IntervalMath(n, n)
        elif isinstance(n, IntervalMath):
            return n
        else:
            raise TypeError\
                  ('operand %s %s must be number or interval' % (n, type(n)))

    def _limits(self, other):
        other = IntervalMath.n2i(other)
        return self.lo, self.up, other.lo, other.up

    def __add__(self, other):
        a, b, c, d = self._limits(other)
        return IntervalMath(a + c, b + d)

    def __sub__(self, other):
        a, b, c, d = self._limits(other)
        return IntervalMath(a - d, b - c)

    def __mul__(self, other):
        a, b, c, d = self._limits(other)
        return IntervalMath(min(a*c, a*d, b*c, b*d),
                            max(a*c, a*d, b*c, b*d))

    def __truediv__(self, other):
        a, b, c, d = self._limits(other)
        # [c,d] cannot contain zero:
        if c*d <= 0:
            raise ValueError\
                  ('Interval %s cannot be denominator because '\
                  'it contains zero')
        return IntervalMath(min(a/c, a/d, b/c, b/d),
                            max(a/c, a/d, b/c, b/d))

    def __radd__(self, other):
        other = IntervalMath.n2i(other)
        return other + self

    def __rsub__(self, other):
        other = IntervalMath.n2i(other)
        return other - self

    def __rmul__(self, other):
        other = IntervalMath.n2i(other)
        return other*self

    def __rtruediv__(self, other):
        other = IntervalMath.n2i(other)
        return other/self

    def __pow__(self, exponent):
        if isinstance(exponent, int):
            p = 1
            if exponent > 0:
                for i in range(exponent):
                    p = p*self
            elif exponent < 0:
                for i in range(-exponent):
                    p = p*self
                p = 1/p
            else:
                p = IntervalMath(1, 1)
            return p
        else:
            raise TypeError('exponent must be int')

    def __eq__(self, other):
        return self.lo == other.lo and self.up == other.up

    def __neq__(self, other):
        return not self.__eq__(other)

    def __float__(self):
        return 0.5*(self.lo + self.up)

    def width_in_percent(self):
        """
        Return the width of the interval as percentage around the mean.
        >>> a = IntervalMath(10*0.9, 10*1.1)  # 10% to either side of 10
        >>> a.width_in_percent()
        20.0
        """
        m = float(self)
        w2 = m - self.lo
        p2 = w2/m*100
        return 2*p2

    def tolist(self):
        return [self.lo, self.up]

    def __str__(self):
        return '[%g, %g]' % (self.lo, self.up)

    def __repr__(self):
        return '%s(%g, %g)' % \
               (self.__class__.__name__, self.lo, self.up)


I = IntervalMath
x=I(1,2)
f=x/(x+1)
print ("Computed interval for f=x/(x+1) for x in %s: %s"%(x,f))
print ("The interval obtained via Calculus is smaller:[0.5, 0.6666]")
print ('This is caused by the "dependency Problem" on Interval arithmetic, but can be solve easily in this case, writing f with x appearing only once.')
f2=1/(1+(1/x))
print ("Computed interval for f=1/(1+1/x) for x in %s: %s, which is not overestimated"%(x,f2))
