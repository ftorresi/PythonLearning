me=9.1094e-31  #e-mass
e=1.6022e-19  #e-charge
epsilon=8.8542e-12 #vaccum electrical permitivity
h=6.6261e-34 #Planck's constant
energylist=[]
for n in range(1,21):
  E=-me*e**4/(8.0*(epsilon*h*n)**2)
  energylist.append(E)
  print "%2i %.2E"%(n, E)
initial1=[]
initial2=[]
initial3=[]
initial4=[]
initial5=[]
print "           1             2             3             4             5"
for n in range(1,6):
  initial1.append(-energylist[n]+energylist[1])
  initial2.append(-energylist[n]+energylist[2])
  initial3.append(-energylist[n]+energylist[3])
  initial4.append(-energylist[n]+energylist[4])
  initial5.append(-energylist[n]+energylist[5])
  print  "%2i  %11.2E   %11.2E   %11.2E   %11.2E   %11.2E" %(n, initial1[n-1], initial2[n-1],initial3[n-1],initial4[n-1],initial5[n-1])

  
