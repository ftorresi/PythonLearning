import numpy as np

x=np.zeros(2)
t=np.zeros(2)

x[0]=0; x[1]=2; t[0]=1; t[1]=1.5

a1=np.sin(x)
a2=np.cos(a1)
a3=1.0/t
a4=np.exp(a3)
y=a2+a4

print (y)
