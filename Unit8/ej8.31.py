from math import pi, sqrt
import random
import matplotlib.pyplot as plt

def MCint3(f, a, b, n, N=100):
    s = 0
    # Store every N intermediate integral approximations in an
    # array I and record the corresponding k value.
    I_values = []
    k_values = []
    for k in range(1, n+1):
        x = random.uniform(a, b)
        s += f(x)
        if k % N == 0:
            I = (float(b-a)/k)*s
            I_values.append(I)
            k_values.append(k)
    return k_values, I_values


def func(x):
    return 2/sqrt(1-x**2)

##int(2/sqrt(1-x**2))=2*arcsen(x), which is pi if we integrate from 0 to 1. We evaluate the integral via Monte Carlo
    
step,pie=MCint3(func, 0, 1, 10000000, 1000) #record values every 1000 steps
print("Estimated value for pi:%g"%(pie[-1]))
err=abs(pie[-1]-pi)
errel=100*err/pi
print("Error:%g, i.e. %g%%"%(err, errel))

step=[s/1000 for s in step]
plt.plot(step,pie,"b-")
x=[0,max(step)]
y=[pi,pi]
plt.plot(x,y,"r-",label="exact value")
plt.legend()
plt.xlabel("Step number [x1000]")
plt.ylabel("Estimation")
plt.savefig("ej8.31.png")
