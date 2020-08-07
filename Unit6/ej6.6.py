
data = [ #Name, distance, brightness, luminosity
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

starsdata={}

for line in data:
    starsdata[line[0]]={}
    starsdata[line[0]]["distance"]=line[1]
    starsdata[line[0]]["apparent brightness"]=line[2]
    starsdata[line[0]]["luminosity"]=line[3]
    

print(starsdata["Sirius A"]["luminosity"])
print(starsdata["Alpha Centauri C"]["distance"])
print(starsdata["Luyten 726-8 B"]["apparent brightness"])
#print(starsdata)
