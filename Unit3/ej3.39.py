
data = [
("Alpha Centauri A",    4.3,  0.26,      1.56),
("Alpha Centauri B",    4.3,  0.077,     0.45),
("Alpha Centauri C",    4.2,  0.00001,   0.00006),
("Barnard's Star",      6.0,  0.00004,   0.0005),
("Wolf 359",            7.7,  0.000001,  0.00002),
("BD +36 degrees 2147", 8.2,  0.0003,    0.006),
("Luyten 726-8 A",      8.4,  0.000003,  0.00006),
("Luyten 726-8 B",      8.4,  0.000002,  0.00004),
("Sirius A",            8.6,  1.00,      23.6),
("Sirius B",            8.6,  0.001,     0.003),
("Ross 154",            9.4,  0.00002,   0.0005),
]

print "---STARS SORTED ALPHABETICALLY---"
for item in sorted(data): #sort list alphabetically
    print "%-20s %4.1f %9.6f %9.5f" %(item[0], item[1],item[2],item[3])
    
print "---STARS SORTED BY DISTANCE, in light years---"
    
for item in sorted(data, key=lambda obj: obj[1]): #The value of the key parameter should be a function that takes a single argument and returns a key to use for sorting purposes.  
    print "%-20s %4.1f" %(item[0], item[1])

print "---STARS SORTED BY APPARENT BRIGHTNESS---"
for item in sorted(data, key=lambda obj: obj[2]):
    print "%-20s %9.6f" %(item[0], item[2])


print "---STARS SORTED BY LUMINOSITY---"
for item in sorted(data, key=lambda obj: obj[3]):
    print "%-20s %9.5f" %(item[0], item[3])
