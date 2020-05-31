def triple(x):
  return x + x*2

def test_triple():
  assert triple(3) == 9
  assert abs(triple(0.1)-0.3 < 1e-14)
  assert triple([1, 2]) == [1, 2, 1, 2, 1, 2]
  assert triple("hello ") == "hello hello hello "

test_triple()
