from pysketcher import *

class Person(Shape):
    def __init__(self, headcenter, headradius, armangle=40):
        centre, R=headcenter, headradius # radius and centre of head
        cx,cy=centre
        theta=armangle*pi/180
        alpha=15*pi/180 #legs angle
        
        head=Circle(center=centre, radius=R)
        torso=Line((cx,cy-5*R),(cx,cy-R))
        rleg=Line((cx+6*R*sin(alpha),cy-5*R-6*R*cos(alpha)),(cx,cy-5*R))
        lleg=Line((cx-6*R*sin(alpha),cy-5*R-6*R*cos(alpha)),(cx,cy-5*R))
        rarm=Line((cx,cy-1.8*R),(cx+4*R*sin(theta),cy-1.8*R-4*R*cos(theta)))
        larm=Line((cx,cy-1.8*R),(cx-4*R*sin(theta),cy-1.8*R-4*R*cos(theta))) 
        
        legs = Composition({'lleg': lleg, 'rleg': rleg})
        arms = Composition({'rarm': rarm, 'larm': larm})
        body = Composition({'head': head, 'torso': torso})
        person = Composition({'body': body, 'legs': legs, 'arms':arms})
        
        self.shapes={'person':person}

R=3.25  
cx=-30*R
cy=173*R #using "strange" values to test the class

ymin=cy-11*R
ymax =cy+1.5*R
xmax=cx+4*R
xmin=cx-4*R
drawing_tool.set_coordinate_system(xmin=xmin, xmax=xmax,
                                   ymin=ymin, ymax=ymax,
                                   axis=False)
p=Person((cx,cy),R,45)
p.draw()
drawing_tool.display()
#input()
drawing_tool.savefig('ej9.21.png')
#drawing_tool.savefig('ej9.21.pdf')
