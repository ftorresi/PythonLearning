import numpy as np

def p_L(x, xp, yp):
    pL=0.0
    xp=np.asarray(xp)
    yp=np.asarray(yp)
    if not xp.size == yp.size:
        print("Both data arrays must have the same size")
    else:
        for k in range(xp.size):
            pL+=yp[k]*L_k(x, k, xp, yp)
        return pL
    
    
    
def L_k(x, k, xp, yp):
    Lk=1.0
    for i in range(xp.size):
        if i != k:
            Lk*=(x-xp[i])/(xp[k]-xp[i])
    return Lk

def test_p_L():
    xq=np.linspace(0,np.pi,5)
    yq=np.sin(xq)
    for j in range(xq.size): 
        yout=p_L(xq[j], xq, yq)
        assert abs(yout-yq[j])<1e-10, "The polynomial misses some point(s)"
    x0=(xq[1]+xq[2])/2 #trial point in the middle
    y0=np.sin(x0) #exact value
    ylagrange=p_L(x0, xq, yq)
    print("For x=%.3f, sin(x)=%.4f and the interpolated value with 5 equally spaced points in [0, pi] gives %.4f" %(x0,y0,ylagrange))

test_p_L()

