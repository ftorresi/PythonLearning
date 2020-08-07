
def diff(poly):
    der={}
    for power in poly:
        if power !=0:
            der[power-1]=power*poly[power]
    return der

p = {0: -3, 3: 2, 5: -1} # -3 + 2*x**3 - x**5
dp=diff(p) # should be 6*x**2 - 5*x**4
print(dp)
