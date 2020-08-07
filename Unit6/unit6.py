##example6.1.5

#def read_densities(filename):
    #infile = open(filename, "r")
    #densities = {}
    #for line in infile:
        #words = line.split()
        #density = float(words[-1])
        #if len(words[:-1]) == 2:
            #substance = words[0] + " " + words[1]
        #else:
            #substance = words[0]
        #densities[substance] = density
    #infile.close()
    #return densities
    
#densities = read_densities("unit6.1.5.dat")
#print(densities)
#for key in sorted(densities): #using of sort
    #print (key, densities[key])


##example6.1.6

#infile = open('unit6.1.6.dat', 'r')
#lines = infile.readlines()
#infile.close()
#data = {}   #  data[property][measurement_no] = propertyvalue
#first_line = lines[0]
#properties = first_line.split()
#for p in properties:  #create key p and assign a dict. to each
    #data[p] = {}

#for line in lines[1:]:
    #words = line.split()
    #i = int(words[0])       # measurement number
    #values = words[1:]      # values of properties
    #for p, v in zip(properties, values):
        #if v != 'no':
            #data[p][i] = float(v)

## Compute mean values
#for p in data:
    #values = data[p].values() #"list" of values of the dict. data[p] for every p
    #data[p]['mean'] = sum(values)/len(values)

#for p in sorted(data):
    #print ('Mean value of property %s = %g' % (p, data[p]['mean']))
    
#print(data)

##example6.2.2

## Load the file into list of lines
#with open("unit6.2.2.dat", "r") as infile:
    #lines = infile.readlines()
    
## Analyze the contents of each line
#pairs = []
## list of (n1, n2) pairs of numbers
#for line in lines:
    #words = line.split()
    #for word in words:
        #word = word[1:-1] # strip off parenthesis
        #n1, n2 = word.split(',')
        #n1 = float(n1); n2 = float(n2)
        #pair = (n1, n2)
        #pairs.append(pair) # add 2-tuple to last row
#print(pairs)

##example6.2.3

#infile = open('unit6.2.3.dat', 'r')
#coor = []  # list of (x,y,z) tuples
#for line in infile:
    #x_start = line.find('x=')
    #y_start = line.find('y=')
    #z_start = line.find('z=')
    #x = line[x_start+2:y_start]
    #y = line[y_start+2:z_start]
    #z = line[z_start+2:]
    #print ('debug: x="%s", y="%s", z="%s"' % (x,y,z))
    #coor.append((float(x), float(y), float(z)))
#infile.close()

#import numpy as np
#coor = np.array(coor)
#print (coor.shape, coor)

##example6.2.3 - another option

#infile = open('unit6.2.3.dat', 'r')
#coor = []  # list of (x,y,z) tuples
#for line in infile:
    #words = line.split('=')
    #x = float(words[1][:-1])
    #y = float(words[2][:-1])
    #z = float(words[3])
    #coor.append((x, y, z))
#infile.close()

#import numpy as np
#coor = np.array(coor)
#print (coor.shape, coor)


###Import and process data from an URL
##Example 6.3.4
#"""
#import urllib.request
#url = 'http://www.worldclimate.com/cgi-bin/data.pl?ref=N38W009+2100+08535W'
#local_file = 'unit6.3.4.html'
#urllib.request.urlretrieve(url, filename=local_file)
##"""
#infile = open(local_file, 'r')
#rainfall = []
#for line in infile:
    #if 'Weather station' in line:
        #station = line.split('</strong>')[0].split('<strong>')[1]
        #print(station)
    #if '<td> mm <td' in line:
        #data = line.split('<td align=right>')
        #data[-1] = data[-1].split('<br>')[0]
        #data = [float(x) for x in data[1:]]

#infile.close()
#print (data)


###Import and process data from a CSV file
##Example 6.4.(2-3-4)

#infile = open('unit6.4.2in.csv', 'r')
#import csv
#table = []
#for row in csv.reader(infile):
    #table.append(row)
#infile.close()

#import pprint
#pprint.pprint(table)

## Transform numbers in table into float objects
## (let first row and first column remain strings)
#for r in range(1,len(table)):
    #for c in range(1, len(table[0])):
        #table[r][c] = float(table[r][c])
#pprint.pprint(table)

## Add a new row with sums
#row = [0.0]*len(table[0])
#row[0] = 'sum'
#for c in range(1, len(row)):
    #s = 0
    #for r in range(1, len(table)):
        #s += table[r][c]
    #row[c] = s
#table.append(row)
#pprint.pprint(table)

#outfile = open('unit6.4.2out.csv', 'w')
#writer = csv.writer(outfile)
#for row in table:
    #writer.writerow(row)
#outfile.close()



##Example 6.4.5
#infile = open('unit6.4.2in.csv', 'r')
#import csv
#table = [row for row in csv.reader(infile)]
#infile.close()

## Convert subtable of numbers (string to float)
#import numpy
#subtable = [[float(c) for c in row[1:]] for row in table[1:]]

#data = {'column headings': table[0][1:],
        #'row headings': [row[0] for row in table[1:]],
        #'array': numpy.array(subtable)}

## Add a new row with sums
#data['row headings'].append('sum')
#a = data['array']   # short form
#data['column sum'] = [sum(a[:,c]) for c in range(a.shape[1])] #a[:,c] means column c of array a

#outfile = open('unit6.4.5out.csv', 'w')
#writer = csv.writer(outfile)
## Turn data dictionary into a nested list first (for easy writing)
#table = a.tolist()   # transform array to nested list
#table.append(data['column sum'])
#table.insert(0, data['column headings'])
#table[0].insert(0,"") #add blank in first row, first column
## Extend table with row headings (a new column)
#[table[r+1].insert(0, data['row headings'][r]) for r in range(len(table)-1)]
#for row in table:
    #writer.writerow(row)
#outfile.close()



###Example 6.4.6
#"""
#As rw_csv_numpy.py, but with easy reading of CSV files
#using numpy.genfromtxt.
#"""
#import numpy as np
#arr = np.genfromtxt('unit6.4.2in.csv', delimiter=',', dtype=str)

#data = {'column headings': arr[0,1:].tolist(),
        #'row headings': arr[1:,0].tolist(),
        #'array': np.asarray(arr[1:,1:], dtype=np.float)}

#data['row headings'].append('sum')
#data['column sum'] = np.sum(data['array'], axis=1).tolist()

#outfile = open('unit6.4.6out.csv', 'w')
#import csv
#writer = csv.writer(outfile)
## Turn data dictionary into a nested list first (for easy writing)
#table = data['array'].tolist()
#table.append(data['column sum'])
#table.insert(0, data['column headings'])
#table[0].insert(0,"") #add blank in first row, first column
## Extend table with row headings (a new column)
#[table[r+1].insert(0, data['row headings'][r])
 #for r in range(len(table)-1)]
#for row in table:
    #writer.writerow(row)
#outfile.close()



###Example 6.4.6 - shorter

#"""
#Read CSV file into numpy array with numpy.genfromtxt,
#extend array with new row with column sums, compute sums,
#write array to CSV file using numpy.savetxt.
#As rw_csv_numpy2.py, but with numpy constructions of output.
#"""

#"""Easy reading of CSV files using numpy.genfromtxt."""
#import numpy as np
#arr = np.genfromtxt('unit6.4.2in.csv', delimiter=',', dtype=str)

## Add row for sum of columns
#arr.resize((arr.shape[0]+1, arr.shape[1])) #add 1 row, same number of columns
#arr[-1,0] = '"sum"'
#subtable = np.asarray(arr[1:-1,1:], dtype=np.float)
#sum_row = np.sum(subtable, axis=1)
#arr[-1,1:] = np.asarray(sum_row, dtype=str) #add sums to last row

## numpy.savetxt writes table with a delimiter between entires
#np.savetxt('unit6.4.6bout.csv', arr, delimiter=',', fmt='%s')



