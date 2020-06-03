def makelist(start, stop, inc):
    value = start
    result = []
    while value <= stop:
        result.append(value)
        value = value + inc
    return result

print makelist(0,100,1) #[0,1,2,...,100]
print makelist(0, 100, 1.0) #[0,1.0,2.0,...,100.0]
print makelist(-1, 1, 0.1) #[-1, -0.9, -0.8,..., 1.0], or close enough
print makelist(10, 20, 20) #[10]
#print makelist([1,2], [3,4], [5]) #Infinite loop
#print makelist((1,-1,1), ("myfile.dat", "yourfile.dat")) #error
# print makelist("myfile.dat", "yourfile.dat", "herfile.dat")  #Infinite loop
