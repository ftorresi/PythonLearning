
class Hello:
    
    def __init__(self):
        self.h="Hello, "
    
    def __str__(self):
        return "Hello, World!"
    
    def __call__(self,st):
        return self.h+st+"!"

a = Hello()
print (a("students")) #Hello, students!
print (a) #Hello, World!
