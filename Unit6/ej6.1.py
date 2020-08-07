
def filetodict(filename):
    c_names=[]
    c_values=[]
    dic={}
    with open(filename,"r") as infile:
        infile.readline() #skip 2 lines
        infile.readline()
        
        for line in infile:
            data=line.split()
            name=" ".join(data[0:-2])
            val=float(data[-2])
            c_names.append(name)
            c_values.append(val)
        
        for i in range(len(c_names)):
            dic[c_names[i]]=c_values[i]
        
        return dic



def filetodict2(filename): #after reading example 6.5.1, no need to create auxiliar lists
    infile = open(filename, "r")
    ctt = {}
    infile.readline() #skip 2 lines
    infile.readline()
    for line in infile:
        words = line.split()
        val = float(words[-2])
        if len(words[:-2]) == 2:
            name = words[0] + " " + words[1]
        elif len(words[:-2]) == 3:
            name = words[0] + " " + words[1] + " " + words[2]
        else:
            name = words[0]
        ctt[name] = val
    infile.close()
    return ctt


print (filetodict("ej6.1.dat"))
print (filetodict2("ej6.1.dat"))
