Flist= [10*i for i in range(11)]
Clist= [5.0/9*(f-32) for f in Flist]
print " F   C"
for a1, a2 in zip(Flist, Clist):
 print "%3i %3i" %(a1,a2)
