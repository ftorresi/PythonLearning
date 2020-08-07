import numpy as np
import matplotlib.pyplot as plt


epslist=[]
errlist=[]
nlist=[]

#Read data 
with open("ej6.4.dat","r") as infile:
    for i in range(24):
        infile.readline() #skip 24 lines
    lines = infile.readlines() #read the rest of the file

    for line in lines:
        eps_start=line.find("epsilon:")
        err_start=line.find("error:")
        n_start=line.find("n=")
        
        eps=line[eps_start+9:eps_start+14]
        err=line[err_start+7:err_start+15]
        n=line[n_start+2:]
        
        epslist.append(float(eps))
        errlist.append(float(err))
        nlist.append(int(n))

epsarr=np.array(epslist)
errarr=np.array(errlist)
narr=np.array(nlist)




#Plot 
plt.plot(narr,epsarr,"o:",label="epsilon")
plt.plot(narr,errarr,"o:",label="exact error")
plt.legend()
plt.xlabel("n")
plt.savefig("ej6.4.png")
#plt.show()

