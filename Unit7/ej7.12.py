import numpy as np

class Sum:
    """Given a formula for terms, make a sum from term M to N"""
    
    def __init__(self,f,M,N):
        self.f,self.M,self.N=f,M,N
    
    def __call__(self,x):
        s=0.0
        f,M,N=self.f,self.M,self.N
        for k in range(M,N+1):
            s+=f(k,x)
        return s                  
    
    def term(self,k,x):
        return self.f(k,x)
    
    

def test_Sum():
    def geo(k,x):  #geometric series
        return x**k
    
    x0=0.5
    M=0
    for N in range(10): # Sum up to 10 terms
        expect=(1-x0**(N+1))/(1-x0)
        s=Sum(geo,M,N)
        success=abs(s(x0)-expect)<1e-12
        assert success, "Bug in Sum"
        
        ter_ok=x0**N
        ter=s.term(N,x0)
        success=abs(ter-ter_ok)<1e-12
        assert success, "Bug in Sum.term"


if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        test_Sum()
        
        def term(k, x):
            return (-x)**k

        S = Sum(term, M=0, N=3)
        x = 0.5
        print (S(x))
        print (S.term(k=4, x=x)) # (-0.5)**4
    
    else:
        from math import factorial, pi
        def sintay(k,x):
            if k%2==0:
                return 0
            elif k%4==1:
                return (x**k)/factorial(k)
            elif k%4==3:
                return -(x**k)/factorial(k)
        
        N=10
        Tsin=Sum(sintay,0,N)
        x=pi/6 #Exact value sin(pi/6)=0.5
        print ("x=%g, Taylor_sin(x)=%g for %d terms, exact: sin(x)=0.5" %(x,Tsin(x),N+1))
        for k in range(0,N+1):
            print("Term %g: %g" %(k,Tsin.term(k=k,x=x)))
        
        x=pi #Exact value sin(pi/6)=0
        print ("\nx=%g, Taylor_sin(x)=%g for %d terms, exact: sin(x)=0" %(x,Tsin(x),N+1))
        for k in range(0,N+1):
            print("Term %g: %g" %(k,Tsin.term(k=k,x=x)))
