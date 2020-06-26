import sys

try:
    F = float(sys.argv[1])
except IndexError:
    print "Fahrenheit degrees must be supplied on the command line."
    sys.exit(1)
    
C = (F-32)*5.0/9
print C 
