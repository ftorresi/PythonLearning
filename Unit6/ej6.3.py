
def read_densities(filename):
    infile = open(filename, "r")
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])
        substance=" ".join(words[:-1])
        densities[substance] = density
    infile.close()
    return densities
    
#densities = read_densities("unit6.1.5.dat")
#print ("ice density: %g" %densities["ice"])

#for key in sorted(densities): #use of sorted
    #print (key, densities[key])

def read_densities2(filename):
    infile = open(filename, "r")
    densities = {}
    density_start=15 #numbers start in col. 15 (starting count from 0)
    for line in infile:
        density = float(line[density_start:])
        substance=line[:density_start]
        substance=substance.strip() #remove whitespace
        densities[substance] = density
    infile.close()
    return densities

#densities2 = read_densities2("unit6.1.5.dat")
#print ("ice density: %g" %densities2["ice"])

#for key in sorted(densities2): #use of sorted
    #print (key, densities2[key])
    
def test_readdens():
    d1=read_densities("unit6.1.5.dat")
    d2=read_densities2("unit6.1.5.dat")
    
    checklen=(len(d1)==len(d2))
    msglen="dictionaries length are not the same"
    assert checklen, msglen
    
    key1=sorted(d1)
    key2=sorted(d2)
    for i in range(len(d1)):
        checkkey=(key1[i]==key2[i])
        msgkey='keys in %d position do not coincide: "%s" and "%s"' %(i,key1[i],key2[i])
        assert checkkey, msgkey
        
        checkval=(d1[key1[i]]==d2[key2[i]])
        msgval='values in %d position do not coincide: "%g" and "%g"' %(i,d1[key1[i]],d2[key2[i]])
        assert checkval, msgval
        
test_readdens()        
    
    
