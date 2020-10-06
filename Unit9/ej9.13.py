class Person:
    def __init__(self,name,address=None,phonenum=None,birthdate=None,nationality=None):
        self.name=name
        self.address=address
        self.phonenum=phonenum
        self.birthdate=birthdate
        self.nationality=nationality
        
    def __str__(self):
        s="Name: %s" %self.name
        if self.address is not None:
            s+=", Address: %s" %self.address
        if self.phonenum is not None:    
            s+=", Phone Number: %s" %self.phonenum
        if self.birthdate is not None:
            s+=", Date of Birth: %s" %self.birthdate
        if self.nationality is not None:
            s+=", Nationality: %s" %self.nationality
        return s


class Worker(Person):
    
    def __init__(self,name,address=None,phonenum=None,birthdate=None,nationality=None,company_name=None, company_address=None, job_phone=None):
        Person.__init__(self,name,address,phonenum,birthdate,nationality)
        self.company_name=company_name
        self.company_address=company_address
        self.job_phone=job_phone
    
    def __str__(self):
        s=Person.__str__(self)
        if self.company_name is not None:
            s+=", Company Name: %s" %self.company_name
        if self.company_address is not None:    
            s+=", Company Address: %s" %self.company_address
        if self.job_phone is not None:
            s+=", Job Phone Number: %s" %self.job_phone
        return s
    
class Scientist(Worker):
    def __init__(self,name,address=None,phonenum=None,birthdate=None,nationality=None,company_name=None, company_address=None, job_phone=None,discipline=None,sc_type=None):
        Worker.__init__(self,name,address,phonenum,birthdate,nationality,company_name, company_address, job_phone)
        self.discipline=discipline
        self.sc_type=sc_type
    
    def __str__(self):
        s=Worker.__str__(self)
        if self.discipline is not None:
            s+=", Discipline: %s" %self.discipline
        if self.sc_type is not None:
            if isinstance(self.sc_type,(list,tuple)):
                s+=", Type of scientist: "
                for pos in self.sc_type:
                    s+="%s + " %pos
                s=s[:-3]
            else:
                s+=", Type of scientist: %s" %self.sc_type
        return s   
        
class Researcher(Scientist):
    pass

class Postdoc(Scientist):
    pass

class Professor(Scientist):
    pass
    
if __name__ == '__main__':
    p1=Person("John Doe",phonenum="03413654987",nationality="Argentinian")
    
    p2=Worker("John Doe",phonenum="03413654987",nationality="Argentinian",company_name="Archie", job_phone="03414381142",birthdate="19/05/1988" )
    
    p3=Scientist("John Doe",birthdate="19/05/1988",phonenum="03413654987",nationality="Argentinian",company_name="Archie", job_phone="03414381142",discipline="Chemistry",sc_type=["Experimental","Computational"] )
    
    p4=Professor("Marie Curie", company_name="University of Paris",nationality="Polish",birthdate="07/11/1867",discipline="ChemPhys",sc_type="Experimental")
    
    p5= Postdoc("Miguel Garabal",phonenum="49668900",birthdate="29/02/1980",nationality="Argentinian",company_name="Vorterix", company_address="Lacroze y Alvarez Thomas", job_phone="49668900",discipline="Radio",sc_type="Experimental")
    
    p6=Researcher("Susana Gravia",address="Cochabamba 1028",phonenum="03413796520",birthdate="13/08/1979",nationality="Argentinian",company_name="CONICET", company_address="27 de febrero 210 bis", job_phone="4535142",discipline="Mathematics",sc_type=("Theoretical","Computational"))
    
    for el in [p1,p2,p3,p4,p5,p6]:
        print (el.__class__.__name__)
        print (type(el))
        print(dir(el))
        print(el)
        
        
        
