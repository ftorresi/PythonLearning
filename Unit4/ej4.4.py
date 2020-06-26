infile=open("input4.4.dat","r")
outfile=open("output4.4.dat","w")

infile.readline() # skip the first line
infile.readline() # skip the second line
infile.readline() # skip the third line

outfile.write("   F       C \n")
for line in infile:
    data=line.split()
    F = float(data[2])
    C = (F-32)*5.0/9
    outfile.write("%7.3f %7.3f \n" %(F, C))

infile.close()
outfile.close()
