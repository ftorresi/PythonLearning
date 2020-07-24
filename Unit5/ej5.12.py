import numpy as np
import matplotlib.pyplot as plt

def C(F):
    return (F-32)*5/9.0

def Capp(F):
    return (F-30)/2.0

Fval=np.linspace(-20,120,281)
Cval=C(Fval)
Cappval=Capp(Fval)

plt.plot(Fval, Cval, "k-", label="Exact C(F)")

plt.plot(Fval, Cappval, "r:", label="Approximated C(F)")


plt.legend()
plt.axis([-20, 120, -40, 55]) # [tmin, tmax, ymin, ymax]
plt.xlabel("Fahrenheit")
plt.ylabel("Celsius")
plt.title("C vs C-approx for a range of F")
plt.savefig("ej5.12FC.png")
plt.show()
