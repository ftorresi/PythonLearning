import sys
import calendar

try: 
    y=int(sys.argv[1])
except IndexError:
    print "Year must be provided"
    y=int(raw_input("year=?"))

try: 
    m=int(sys.argv[2])
except IndexError:
    print "Month must be provided"
    m=int(raw_input("month=?"))
    
try: 
    d=int(sys.argv[3])
except IndexError:
    print "Day number must be provided"
    d=int(raw_input("day number=?"))

daynum=calendar.weekday(y, m, d)
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weekday=days[daynum]

print "%g/%g/%g was/will be a %s" %(d,m,y,weekday)
