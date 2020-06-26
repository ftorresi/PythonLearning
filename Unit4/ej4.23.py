import random
import sys
from math import exp, sin, cos, sinh, tan
from math import log as ln

def power3_identity(A=-100, B=100, n=1000):
    ok=0 #number of successful results
    for i in range(n):
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        succ = ((a*b)**3 == a**3*b**3)
        ok+=succ  #if indentity holds, adds one (True==1, False==0) 
    return float(n-ok)/n # return fraction of failures
#print  power3_identity()

def equal(expr1, expr2, A=-100, B=100, n=500):
    """The expressions to be compared must have 2 variables a and b"""
    ok=0 #number of successful results
    for i in range(n):
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        try:
            succ = (eval(expr1) == eval(expr2))
        except ValueError:
            print "Function evaluation error. Check that the interval [A,B] belongs to the function domain"
            return None
        ok+=succ  #if indentity holds, adds one (True==1, False==0) 
    return float(n-ok)/n # return fraction of failures

#print equal("(a*b)**3", "a**3*b**3")
#print equal("exp(a+b)", "exp(a)*exp(b)")
#print equal("ln(a**b)", "b*ln(a)", A=1e-14)

expressions=[("a-b","-(b-a)"),("float(a)/b","1.0/(float(b)/a)"),("(a*b)**4","a**4*b**4"),("(a+b)**2","a**2+2*a*b+b**2"),("(a+b)*(a-b)","a**2-b**2"),("exp(a+b)","exp(a)*exp(b)"),("ln(a**b)","b*ln(a)"),("ln(a*b)","ln(a)+ln(b)"),("a*b","exp(ln(a)+ln(b))"),("1./(1./a+1./b)","a*b/(a+b)"),("a","a*((sin(b))**2+(cos(b))**2)"),("sinh(a+b)","(exp(a)*exp(b)-exp(-a)*exp(-b))/2"),("tan(a+b)","sin(a+b)/cos(a+b)"),("sin(a+b)","sin(a)*cos(b)+sin(b)*cos(a)")]


for bval in (2,100):
    print "   expr1            expr2            failure rate for interval[1,%g]" %bval
    for i in range(len(expressions)):
        rate= equal(expressions[i][0], expressions[i][1], A=1, B=bval)
        print "%-15s %-33s %.3f" %(expressions[i][0],expressions[i][1],rate)
    print ""
