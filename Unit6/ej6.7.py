
humans={}

with open("ej6.7.dat","r") as infile:
    lines = infile.readlines() #read the rest of the file
    #find the columns where each piece of information starts
    homo_start=0
    when_start=lines[0].find("Lived when")
    height_start=lines[1].find("height")
    weight_start=lines[1].find("mass")
    brain_start=lines[0].find("Brain volume")
    
    for line in lines[3:10]: #work with data lines only
        speciesname=line[homo_start:when_start]
        speciesname=speciesname.strip() #delete leading/ending whitespace
        speciesname=speciesname.replace('H.','homo') #replace "H." for "homo"
        humans[speciesname]={}
        
        #Get data for each category
        when=line[when_start:height_start]
        when=when.strip() #delete leading/ending whitespace
        when=when.replace(' ','') ## remove all blanks
        
        height=line[height_start:weight_start]
        height=height.strip() #delete leading/ending whitespace
        height=height.replace(' ','') ## remove all blanks
        
        weight=line[weight_start:brain_start]
        weight=weight.strip() #delete leading/ending whitespace
        weight=weight.replace(' ','') ## remove all blanks

        brain=line[brain_start:]
        brain=brain.strip() #delete leading/ending whitespace
        brain=brain.replace(' ','') ## remove all blanks
        
        #store data:
        humans[speciesname]["when"]=when
        humans[speciesname]["height"]=height
        humans[speciesname]["mass"]=weight
        humans[speciesname]["brain volume"]=brain
        
outfile=open("ej6.7.out","w")
outfile.write("Species               Lived when    Adult        Adult      Brain volume \n")
outfile.write("                      (mill. yrs)   height (m)   mass (kg)  (cm**3) \n")
outfile.write("-------------------------------------------------------------------------------- \n")
for key in humans.keys():    
    outfile.write("%-22s %-12s %-12s %-10s %s \n" %(key, humans[key]["when"],humans[key]["height"],humans[key]["mass"],humans[key]["brain volume"]))
outfile.write("-------------------------------------------------------------------------------- \n")




















