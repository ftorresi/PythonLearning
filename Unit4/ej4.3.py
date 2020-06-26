infile=open("input4.3.dat","r")

infile.readline() # skip the first line
infile.readline() # skip the second line
infile.readline() # skip the third line

line4=infile.readline()
data=line4.split()
F = float(data[2])

C = (F-32)*5.0/9
print C 

infile.close()
