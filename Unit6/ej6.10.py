#representation of -0.5+2*x**100 in list and dict


polylist=[0]*101
polylist[0]=-0.5
polylist[100]=2.

polydict={0:-0.5,100:2.}


print(polylist)
print(polydict)


def eval_poly_list(poly,x):
    return sum([poly[i]*x**i for i in range(len(poly))])

def eval_poly_dict(poly,x):
    return sum([poly[power]*x**power for power in poly])

x=1.05
print(eval_poly_list(polylist,x))
print(eval_poly_dict(polydict,x))
