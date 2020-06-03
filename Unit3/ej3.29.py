def H(x):
    return (0 if x<0 else 1)

def test_H():
    v=[H(-10),H(-10**(-15)), H(0),H(10**(-15)),H(10)]
    exp=[0,0,1,1,1]
    suma=0
    for ov,ev in zip(v,exp):
        suma+=abs(ov-ev)
    success=suma<1e-14
    msg= "Function poorly defined"
    assert success, msg

test_H()
