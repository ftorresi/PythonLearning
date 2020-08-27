class Rope:
    
    def __init__(self,n):
        self.r=n
    
    def __str__(self):
        return "%g" %self.r
    
    def __add__(self,other):
        s=self.r+other.r+1
        return (Rope(s))
    

rope1 = Rope(2)
rope2 = Rope(2)
rope3 = rope1+rope2
print (rope3)
