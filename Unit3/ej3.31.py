def ind1(x,L=0,R=1):
    return (1 if L<=x<=R else 0)


def H(x):
    return (0 if x<0 else 1)

def ind2(x,L=0,R=1):
    return H(x-L)*H(R-x)


def test_ind():
    xval=(-1,0,0.5,1,2)
    expect=(0,1,1,1,0)
    obtain1=[ind1(x) for x in xval]
    obtain2=[ind2(x) for x in xval]
    suma=0.0
    for ov,ev in zip(obtain1,expect):
        suma+=abs(ov-ev)
    success=suma<1e-14
    msg= "Function ind1 poorly defined"
    assert success, msg
    suma=0.0
    for ov,ev in zip(obtain2,expect):
        suma+=abs(ov-ev)
    success=suma<1e-14
    msg= "Function ind2 poorly defined"
    assert success, msg
    
    
    
test_ind()

#print ind1(-1), ind2(-1)
#print ind1(0), ind2(0)
#print ind1(0.5), ind2(0.5)
#print ind1(1), ind2(1)
#print ind1(2), ind2(2)
