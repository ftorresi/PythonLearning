def L4(x, n=None, epsilon=None, return_n=False):
    if n is not None:
        if epsilon is not None:
            print "n OR epsilon must be given, not both"
            return None
        else:    #if n is given
            s = 0
            for i in range(1, n+1):
                s += (1.0/i)*(x/(1.0+x))**i
            return s
    else:
        if epsilon is None:
            print "n or epsilon must be given"
            return None
        else: #if epsilon is given
            x = float(x)
            i = 1
            term = (1.0/i)*(x/(1+x))**i
            s = term
            while abs(term) > epsilon:
                i += 1
                term = (1.0/i)*(x/(1+x))**i
                s += term
            if return_n: #return value and n
                return s, i
            else:        #return value only
                return s

value, n = L4(1.718281828, epsilon=1E-8, return_n=True)
print value, n
value = L4(1.718281828, epsilon=1E-8, return_n=False)
print value
value = L4(1.718281828, n=50)
print value
value = L4(1.718281828)
value = L4(1.718281828, epsilon=1E-8, n=30)

