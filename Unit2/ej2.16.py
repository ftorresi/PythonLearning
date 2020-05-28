Flist= [10*i for i in range(11)]
Clist= [5.0/9*(f-32) for f in Flist]
Caprox= [0.5*(f-30) for f in Flist]
print " F     C   Capprox"
for a1, a2, a3 in zip(Flist, Clist, Caprox):
 print "%3g %6.2f %5.1f" %(a1,a2,a3)

print "-------------------"

conversion=[]
for i in range(len(Flist)):
   elem=[Flist[i],Clist[i],Caprox[i]]
   conversion.append(elem)

print " F     C   Capprox"
for l in conversion:
   print "%3g %6.2f %5.1f" %(l[0],l[1],l[2])
