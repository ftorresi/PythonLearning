#v0 = 5
#g = 9.81
#t = 0.6
#y = v0*t - 0.5*g*t**2

#print """
#At t=%f s, a ball with
#initial velocity v0=%.3E m/s
#is located at the height %.2f m.
#""" % (t, v0, y)

########################
#C = 21
#F = (9./5)*C + 32
#print F
########################

#i = 62
#r = 189876545.7654675432

## Print out numbers with quotes "" such that we see the
## width of the field
#print '"%d"' % i       # minimum field
#print '"%5d"' % i      # field of width 5 characters
#print '"%05d"' % i     # pad with zeros

#print '"%g"' % r       # r is big number so this is scientific notation
#print '"%G"' % r       # E in the exponent
#print '"%e"' % r       # compact scientific notation
#print '"%E"' % r       # compact scientific notation
#print '"%20.2E"' % r   # 2 decimals, field of width 20
#print '"%30g"' % r     # field of width 30 (right-adjusted)
#print '"%-30g"' % r    # left-adjust number
#print '"%30.4g"' % r  # 3 decimals

#print '%s' % i   # can convert i to string automatically
#print '%s' % r

## Use %% to print the percentage sign
#print '%g %% of %.2f Euro is %.2f Euro' % \
      #(5.1, 346, 5.1/100*346)
#####################

v0 = 5
g = 9.81
yc = 0.2
from math import *
t1 = (v0 - sqrt(v0**2 - 2*g*yc))/g
t2 = (v0 + sqrt(v0**2 - 2*g*yc))/g
print """\
At t=%g s and %g s, 
the height is %g m.\
""" % (t1, t2, yc)
