q = [["a", "b", "c"], ["d", "e", "f"], ["g", "h"]]
a1=q[0][0]
a2=q[1]
a3=q[-1][-1]
a4=q[1][0]
a5=q[-1][-2]

print "a1) %s  a2) %s  a3) %s  a4) %s" %(a1, a2, a3, a4)
print "q[-1][-2] has value %s since it's the second-to-last element in the last list" %a5
