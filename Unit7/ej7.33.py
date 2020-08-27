#I'm assuming that the input for each class is the dictionary created in example 6.7.2
#What's needed is not clear to me after reading the exercise, so...

class Student:
    def __init__(self,name, courselist):  #courselist=dict[name]
        self.name=name
        self.stinfo=courselist
        
    def __str__(self):
        s = ("Name: %s\n" %self.name)
        for elem in self.stinfo:
            s+="%-20s %-12s %3s %2s\n" %(elem['title'], elem['semester'], elem['credit'], elem['grade'])
        return s    
    
    
class Course:
    def __init__(self,coursename, coursedic):  #coursedic=dic w/all the data
        self.name=coursename
        self.coursedata=[]
        for key in coursedic:    #for every student
            for elem in coursedic[key]:  #for every course on that student
                if coursename==elem["title"]:  #if the course is there
                    print(key, elem, coursename)
                    d={"student":key,"semester":elem["semester"], "credit":elem["credit"], "grade":elem["grade"]}
                    self.coursedata.append(d)
        
    def __str__(self):
        s = ("Course: %s\n" %self.name)
        for elem in self.coursedata:
            s+="%-20s %-12s %3s %2s\n" %(elem['student'], elem['semester'], elem['credit'], elem['grade'])
        return s  
            
dic={}
dic["Juan"]=[{"title":"Physics","semester":"fall 2011", "credit":"10", "grade":"B"},{"title":"Biology","semester":"fall 2012", "credit":"15", "grade":"A"}]
dic["Pedro"]=[{"title":"Physics","semester":"spring 2010", "credit":"10", "grade":"A"},{"title":"Chemistry","semester":"fall 2011", "credit":"10", "grade":"B"}]

j=Student("Juan",dic["Juan"])
p=Student("Pedro",dic["Pedro"])

print(j)
print(p)

k=Course("Physics",dic)

print(k)
            
