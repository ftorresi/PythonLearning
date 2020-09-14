import random

class Hat:
    def __init__(self,**kwargs):
        balls=[]
        for color in kwargs:
            for i in range(kwargs[color]):
                balls.append(color)
        self.balls=balls
        
    def draw(self,n):
        """Draw n balls using list index."""
        selected=[]
        for i in range(n):
            index = random.randint(0, len(self.balls)-1)
            color = self.balls.pop(index) #select color and remove it from hat
            selected.append(color)
        return selected
    
    def putback(self, color):
        """Put (back) a ball in the hat."""
        self.balls.append(color)
        
    def __str__(self):
        return str(self.balls)
         
        
#h=Hat(red=3, blue=4, green=6)
#print(h)
#print(h.draw(3))

N =int(input('How many experiments? '))
w=0
for i in range(N):
    hat=Hat(brown=8, blue=6, green=3)
    balls=hat.draw(6)
    if balls.count('brown')>=2 and balls.count('blue')>=2: #I guess it's AT LEAST 2 blue and 2 brown balls (otherwose it'd say 2 of each color)
        w+=1
p=100*w/N
print("The probability of getting 2 brown and 2 blue balls\nwhen drawing 6 balls from a hat with 6 blue, 8 brown,\nand 3 green balls is %5.2f%%"%p)
