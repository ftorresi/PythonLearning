from math import factorial as fact

def binomial(x,n,p=0.5):
    coef=fact(n)/(fact(x)*fact(n-x))
    binom=coef*(p**x)*(1-p)**(n-x)
    return binom


caseb=binomial(2,5,0.5)
print "The probability of getting two heads when flipping a coin five times is %.4f" %caseb

casec=binomial(4,4,1.0/6)
print "The probability of getting four ones in a row when throwing a dice is %.4f" %casec


cased=binomial(0,5,1./120)
cased=1-cased
print "The probability that a skier will experience a ski break during five competitions is %.4f" %cased
