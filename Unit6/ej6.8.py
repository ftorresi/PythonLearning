import numpy as np
import matplotlib.pyplot as plt


#Read data to nested list
mu_data = {}
with open("ej6.8.dat","r") as infile:
    for i in range(8):
        infile.readline() #skip 8 lines
    lines = infile.readlines() #read the rest of the file
    #print (lines)
    first_line=lines[0]
    propnames=first_line.split() #interest in the last 3 values
    
    for line in lines[1:-2]: #avoid 1st and last 2 lines
        words = line.split()
        gas=words[0]
        if len(words[:-3])==2: #gas name has 2 words
            gas=words[0]+" " +words[1]
        mu_data[gas]={}
        mu_data[gas][propnames[-1]]=float(words[-1])
        mu_data[gas][propnames[-2]]=float(words[-2])
        mu_data[gas][propnames[-3]]=float(words[-3])

#define function mu
def mu(T, gas, mu_data):
    
    C=mu_data[gas]["C"]
    T_0=mu_data[gas]["T_0"]
    mu_0=mu_data[gas]["mu_0"]
    mu=mu_0*(T_0+C)/(T+C)*(T/T_0)**1.5  #WARNING: there's a mistake in the book's formula
    
    return mu

#Plot mu 
Tlist=np.linspace(223,373,1501)
for gas in ("air","carbon dioxide", "hydrogen"):
    y=mu(Tlist, gas, mu_data)
    plt.plot(Tlist,y,label=gas)
plt.legend()
plt.xlabel("T [Kelvin]")
plt.ylabel("Viscosity [10**-6 Pa*s]")
plt.savefig("ej6.8.png")
#plt.show()

