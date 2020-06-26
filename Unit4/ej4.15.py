def halve(x):
    return x/2



def test_halve():
    assert halve(5.0) == 2.5 # Real number division
    assert halve(5) == 2 # Integer number division

test_halve()

###Part b

def add(x,y):
    return x+y


def test_add():
    # Test integers
    assert add(1, 2) == 3
    
    # Test floating-point numbers with rounding error
    tol = 1E-14
    a = 0.1; b = 0.2
    computed = add(a, b)
    expected = 0.3
    assert abs(expected - computed) < tol
    
    # Test lists
    assert add([1,4], [4,7]) == [1,4,4,7]
    
    # Test strings
    assert add("Hello, ", "World!") == "Hello, World!"

test_add()

###Part c

def equal(s1,s2):
    if s1==s2:
        return True, s1
    else:
        s=[]
        l=min(len(s1),len(s2))
        for i in range(l):
            s.append(s1[i])
            if s1[i]!=s2[i]:
                s.append("|")
                s.append(s2[i])
        d= len(s1)-len(s2)
        for i in range(abs(d)):
          if d>0:
                 s.append(s1[l+i])
                 s.append("|*")
          else: #if d=0 doesn't enter the loop
                 s.append("*|")
                 s.append(s2[l+i])
        st="".join(s)
        return False, st
    
def test_equal():
    assert equal("abc", "abc") == (True, "abc")
    assert equal("abc", "aBc") == (False, "ab|Bc")
    assert equal("abc", "aBcd") == (False, "ab|Bc*|d")
    assert equal("abcde", "abcd") == (False, "abcde|*")
    assert equal("Hello, World!", "hello world") == \
        (False, "H|hello,|  |wW|oo|rr|ll|dd|*!|*")
test_equal()


