from math import sin, pi

def H_eps(x,eps=0.01):
    if x<-eps:
        return 0
    elif x>eps:
        return 1
    else:
        return 0.5+x/(2*eps)+sin(pi*x/eps)/(2*pi)


    

def test_H_eps():
    v=[H_eps(-0.1), H_eps(-0.01), H_eps(0), H_eps(0.01), H_eps(0.1)]
    exp=[0,0,0.5,1,1]
    suma=0
    for ov,ev in zip(v,exp):
        suma+=abs(ov-ev)
    success=suma<1e-14
    msg= "Function poorly defined"
    assert success, msg

test_H_eps()
