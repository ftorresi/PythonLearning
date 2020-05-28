
def double(x):
  return x*2

def test_double():
  assert double(2) == 4
  assert abs(double(0.1) - 0.2) < 1E-15
  assert double([1, 2]) == [1, 2, 1, 2]
  assert double((1, 2)) == (1, 2, 1, 2)
  assert double(3+4j) == 6+8j
  assert double("hello") == "hellohello"

test_double()

#print F(C(0))
#print C(F(0))
#print F(C(5))
#print C(F(5))


