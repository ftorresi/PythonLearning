Flist= [10*i for i in range(11)]
Clist= [5.0/9*(f-32) for f in Flist]
Caprox= [0.5*(f-30) for f in Flist]
print " F     C   Capprox"
for a1, a2, a3 in zip(Flist, Clist, Caprox):
 print "%3g %6.2f %5.1f" %(a1,a2,a3)
