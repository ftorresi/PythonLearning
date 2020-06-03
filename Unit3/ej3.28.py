lista=[90.001,0,-1,8.3,90.001,-100,-3518.3]

def mymax(a):
  maxval=a[0]
  for el in a[1:]: #evaluate in the rest of the values
    maxval=(el if el > maxval else maxval) #to keep only the highest value
  return maxval

def mymin(a):
  minval=a[0]
  for el in a[1:]: #evaluate in the rest of the values
    minval=(el if el < minval else minval) #to keep only the lowest value
  return minval

print mymax(lista), max(lista)
print mymin(lista), min(lista)






