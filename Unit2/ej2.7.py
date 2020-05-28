a=18
b=188
n=10
coord=[]
h=(b-a)/float(n)

#part A
for i in range(1+n):
  x=a+i*h
  coord.append(x)
print coord

#part B
coordB=[a+i*h for i in range(1+n)]
print coordB
