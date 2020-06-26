import sys

def readdata(filename):
    infile=open(filename,"r")
    l1=infile.readline() #v0 in line 1, 2nd word
    vdata=l1.split()
    v0=float(vdata[1])
    infile.readline() #skip line 2
    t=[]
    for line in infile:
        times=line.split()
        for time in times:
            t.append(float(time))
    infile.close()
    return v0, t

#v0, t=readdata("input4.14.dat")
#print v, t0


###Part 2
def readdata_test():
    dummyfile=open("qdummy4.14.dat","w")
    dummyfile.write("v0: 4.9 \n")
    dummyfile.write("t:\n")
    for h in range(20):
        dummyfile.write("%g  " %(0.05*h) )
        if(h%7==0): 
            dummyfile.write("\n") #make new line every 7 timesm starting with 0
    dummyfile.close()
    vo, to=readdata("qdummy4.14.dat")
    success= abs(vo-4.9) < 1e-14
    msg= "function fails reading v0"
    assert success, msg
    for h in range(20):
        success=abs(0.05*h-to[h])<1e-14
        msg= "function fails reading times"
        assert success, msg
#readdata_test()

###Part 3
def tycols(filein,fileout):
    outfile=open(fileout,"w")
    g = 9.81
    v0, t=readdata(filein)
    t.sort()
    outfile.write("  t       y\n")
    for time in t:
        y=v0*time - 0.5*g*time**2
        outfile.write("%6.3f %7.3f\n" %(time,y))

tycols("input4.14.dat","output4.14.dat")
    
    



