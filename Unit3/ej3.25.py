def fact(n):
    if ((type(n)!= int) or (n<0)):
        return "argument must be a non-negative integer!"
    elif (n==0 or n==1):
        return 1
    else:
        fac=1
        for i in range (1,n+1):
            fac*=i
        return fac
    
def test_fact():
  # Check an arbitrary case
  n = 4
  expected = 4*3*2*1
  computed = fact(n)
  assert computed == expected
  # Check the special cases
  assert fact(0) == 1
  assert fact(1) == 1
