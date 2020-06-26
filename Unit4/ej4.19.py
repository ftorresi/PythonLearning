import sys

try:
    C = float(sys.argv[1])
except NameError:
    print "module sys not imported in the program"
    sys.exit(1)
except AttributeError:
    print "Error in list name in a module"
    sys.exit(1)
except IndexError:    
    print "C must be provided as command-line argument"
    sys.exit(1)
