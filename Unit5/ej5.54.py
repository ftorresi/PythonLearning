import numpy as np

def test_addition(): #test matrix addition A+B=B+A 
    n = 4 # matrix size
    A = np.matrix(np.random.rand(n, n))
    B = np.matrix(np.random.rand(n, n))
    tol = 1E-14
    result1 = A + B
    result2 = B + A
    assert abs(result1 - result2).max() < tol


def test_distributive(): #test distributive prop (A+B)C=AC+BC
    n = 4 # matrix size
    A = np.matrix(np.random.rand(n, n))
    B = np.matrix(np.random.rand(n, n))
    C = np.matrix(np.random.rand(n, n))
    tol = 1E-14
    result1 = (A + B)*C
    result2 = A*C + B*C
    assert abs(result1 - result2).max() < tol
    
    
def test_asoc(): #test asociative prop (AB)C=A(BC)
    n = 4 # matrix size
    A = np.matrix(np.random.rand(n, n))
    B = np.matrix(np.random.rand(n, n))
    C = np.matrix(np.random.rand(n, n))
    tol = 1E-14
    result1 = (A*B)*C
    result2 = A*(B*C)
    assert abs(result1 - result2).max() < tol
    
def test_rank(): #test rankA=rank(A^T)
    n=4
    A = np.matrix(np.random.rand(n, n))
    B= A.T #transpose A
    tol = 1E-14
    U,s,V=np.linalg.svd(A) # s are the singular values of A
    # abs(s) > tol gives an array with True and False values
    # s.nonzero() lists indices k so that s[k] != 0
    result1=np.shape((abs(s) > tol).nonzero())[1] # rank
    
    U,s,V=np.linalg.svd(A)
    result2=np.shape((abs(s) > tol).nonzero())[1] # rank
    assert abs(result1 - result2) < tol

def test_det(): #test det(AB)=detA*detB
    n = 4 # matrix size
    A = np.matrix(np.random.rand(n, n))
    B = np.matrix(np.random.rand(n, n))
    C=A*B
    tol = 1E-14
    result1=np.linalg.det(A)*np.linalg.det(B)
    result2=np.linalg.det(C)
    assert abs(result1 - result2) < tol

def test_eigen(): #test rankA=rank(A^T)
    n=4
    A = np.matrix(np.random.rand(n, n))
    B= A.T #transpose A
    tol = 1E-14
    eig_values, eig_vectors = np.linalg.eig(A)
    result1=np.sort(eig_values) #sort eigenvalues
    eig_values, eig_vectors = np.linalg.eig(A)
    result2=np.sort(eig_values) #sort eigenvalues
    assert abs(result1 - result2).max() < tol

test_addition()
test_distributive()
test_asoc()
test_rank()
test_det()
test_eigen()
