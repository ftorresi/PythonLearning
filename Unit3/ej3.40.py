"""Find all prime numbers up to n"""
from math import sqrt

def p(n):
    lis=range(n+1)
    lis[1]=0 #Take 1 as non prime
    end=int(sqrt(n))
    for i in range(2,end+1):
        top=n/i
        for j in range(i,top+1):
            lis[i*j]=0 #i*j is not prime
    tot=0
    for el in lis:
        if el:
            tot+=1
            print el   #print non-zero (i.e., primes)
    print "%g primes were found up to %g" %(tot, n) #as a bonus, gives how many primes were found

p(10000)
