"""
Module for converting among C F and K
Some examples:
C2F(0)
32.0

F2C(212)
100.0

C2K(0)
273.15

K2C(100)
-173.15

F2K(100)
310.9277777777777

 K2F(0)
 -459.67
"""
import sys
_filename = sys.argv[0]
_usage = """
Usage: %s 27.0 F
Program computes the temperature and prints conversion to different units (C, F or K)""" % _filename

def C2F(c):
    return (9.0/5)*c+32
    
def F2C(f):
    return (f-32)*5.0/9

def C2K(c):
    return c+273.15

def K2C(k):
    return k-273.15

def F2K(f):
    return (f-32)*5.0/9+273.15

def K2F(k):
    return (k-273.15)*(9.0/5)+32

def test_conversion():
    #compatible values
    k=273.15; c=0.0; f=32.0
    c1=K2C(k)
    c2=F2C(f)
    f1=C2F(c)
    f2=K2F(k)
    k1=C2K(c)
    k2=F2K(f)
    
    def float_eq(a, b, tolerance=1E-12):
        """Return True if a == b within the tolerance."""
        return abs(a - b) < tolerance
    
    success= float_eq(c,c1) and float_eq(c,c2) and \
             float_eq(k,k1) and float_eq(k,k2) and \
             float_eq(f,f1) and float_eq(f,f2)
    msg="""Computations failed (correct answers in parenthesis):
    c1= %.2f; c2= %.2f (%.2f)
    k1= %.2f; k2= %.2f (%.2f)
    f1= %.2f; f2= %.2f (%.2f)""" %(c1, c2, c, k1, k2, k, f1, f2, f)
    assert success, msg
    
def compute_conversion(temp):
    try:
        temp[0]=float(temp[0])
    except:
        print _usage
        sys.exit(1)
    if temp[1]=="C":
        c=temp[0]
        k=C2K(c)
        f=C2F(c)
        print "%.2f C are %.2f F and %.2f K" %(c,f,k)
    elif temp[1]=="F":
        f=temp[0]
        k=F2K(f)
        c=F2C(f)
        print "%.2f F are %.2f C and %.2f K" %(f,c,k)
    elif temp[1]=="K":
        k=temp[0]
        f=K2F(k)
        c=K2C(k)
        print "%.2f K are %.2f C and %.2f F" %(k,c,f)
    else:
        print _usage
        sys.exit(1)

        

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print _usage
    elif len(sys.argv) == 2:
        if sys.argv[1] == "verify":
            test_conversion()
        else:
            print _usage
    else:
        temp=sys.argv[1:]
        compute_conversion(temp)

