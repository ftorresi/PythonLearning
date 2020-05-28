#part a)
def sum_1k(M):
  s=0.0
  for i in range(1,M+1):
    s+=1/float(i)
  return s

#part b)
def test_sum_1k():
  expected = 1.0+1/2.0+1/3.0+6
  success = abs(sum_1k(3)-expected) < 1e-14
  msg="sum_1k fails for M=3 :( "
  assert success, msg

test_sum_1k()
