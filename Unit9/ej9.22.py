from pysketcher import *

class Person(Shape):
    def __init__(self, headcenter, headradius, armangle=40):
        self.centre, R=headcenter, headradius # radius and centre of head
        self.R=R
        cx,cy=self.centre
        theta=armangle*pi/180
        alpha=15*pi/180 #legs angle
        
        head=Circle(center=self.centre, radius=R)
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
        
    def movearms(self,newangle):
        self.__init__(self.centre, self.R,newangle)

R=1 
cx=4*R
cy=11*R 

ymin=cy-11*R
ymax =cy+1.5*R
xmax=cx+4*R
xmin=cx-4*R
drawing_tool.set_coordinate_system(xmin=xmin, xmax=xmax,
                                   ymin=ymin, ymax=ymax,
                                   axis=False)

import numpy
t1=list(range(24))
t2=list(range(24,0,-1))
tp=t1+t2

p=Person((cx,cy),R,15)

def move(t,fig):
    armsangle = 20+5*t #start in 20° and move every 5°
    fig.movearms(armsangle)


files = animate(p, tp, move, moviefiles=True, pause_per_frame=0)

files_wildcard = files.split('%')[0] + '*.png'
os.system('convert -delay 20 %s* ej9.22waving.gif' % (files_wildcard))
    
    
    
    
#p=Person((cx,cy),R,20)
##p.draw()
#p.movearms(90)
#p.draw()
#drawing_tool.display()
#input()
##drawing_tool.savefig('ej9.22.png')
##drawing_tool.savefig('ej9.22.pdf')
