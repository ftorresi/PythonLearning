import sys
from scitools.StringFunction import StringFunction
from math import pi, sin

if len(sys.argv)==1:
    print("Filename with first line: '<expression> is a function of <list1> with parameter <list2>' must be provided. Optionally, such line may be provided on the command line")
    sys.exit(1)

elif len(sys.argv)==2:
    filename=sys.argv[1]
    with open(filename,"r") as infile:
        sentence=infile.readline()
else:
    sentence=" ".join(sys.argv[1:]) #<expression> is function of <list1> with parameters <list2>

expression, independent_variables=sentence.split("is a function of") #separate expression from the rest

param=""
if independent_variables.find("with parameter")!=-1: #i.e., there are parameters
    independent_variables, param=independent_variables.split("with parameter")
    param=param.strip() #eliminate whitespace
    param=", "+param #if param exists, starts with a comma
    

expression=expression.strip() #eliminate whitespace
independent_variables=independent_variables.strip()

def createfunc(expression,independent_variables,param):
    strfuncarg="'%s', independent_variable='%s'%s" %(expression, independent_variables, param)
    #print(strfuncarg)

    strtoeval="StringFunction(%s)" %strfuncarg
    #print(strtoeval)

    f=eval(strtoeval)   
    return f

#func=createfunc(expression,independent_variables,param)
#print(func(1))

#def test_prog():
    ##test values for x*sin(x) between 0 and 1
    #testfunc=createfunc(expression,independent_variables,param)
    #goal=lambda x: 0.1*x*sin(2*x)
    #for i in range(101):
        #x=0.01*i
        #success=goal(x)==testfunc(x)
        #msg="Failure in 0.1*x*sin(2x) for x=%.2f. For this to work, the input must be: 'A*x*sin(kx)' is a function of x with parameter A=0.1, k=2" %x
        #assert success, msg
    
#test_prog()    
