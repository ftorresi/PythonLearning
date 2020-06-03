## series with c(i,x)=a(i,x)*c(i-1,x) with a(i,x)=(((i-1)/i)*(x/(x+1)))

def L3(x, epsilon=1.0E-6): #original L3
  x = float(x)
  i = 1
  term = (1.0/i)*(x/(1+x))**i
  s = term
  while abs(term) > epsilon:
    i += 1
    term = (1.0/i)*(x/(1+x))**i
    s += term
  return s, i

def L3_ci(x, epsilon=1.0E-6):  #new L3
  x = float(x)
  i = 1
  term = (1.0/i)*(x/(1+x))**i
  s = term
  while abs(term) > epsilon:
    i += 1
    a=((float(i-1)/i)*(x/(x+1)))
    term = a*term
    s += term
  return s, i


#Check L3_ci, given correct L3 
def test_L3_ci():  #compare L3 and L3:ci for several epsilon and x
    for x in range(2,20):
      for k in range(4, 14, 2):
          epsilon = 10**(-k)
          ok=L3(x, epsilon)
          new=L3_ci(x, epsilon)
          success=abs(ok[0]-new[0])<1e-14
          msg="L3_ci fails for x=%g epsilon: %.1E" %(x,epsilon)
          assert success, msg
          print x, epsilon, ok, new

test_L3_ci()
