from pysketcher import *

R = 1    # radius of head
alpha=15*pi/180 #legs angle
H =6*R*(1+cos(alpha))   # height of body
theta=40*pi/180 #arm-torso angle

ymax =0.5*R+H
xmax=8.5*R
xmin=-0.5*R
drawing_tool.set_coordinate_system(xmin=xmin, xmax=xmax,
                                   ymin=-1, ymax=ymax,
                                   axis=False)

head=Circle(center=(4*R,H-R), radius=R)
torso=Line((4*R,H-6*R),(4*R,H-2*R))
rleg=Line((4*R+6*R*sin(alpha),0),(4*R,H-6*R))
lleg=Line((4*R-6*R*sin(alpha),0),(4*R,H-6*R))
rarm=Line((4*R,H-2.8*R),(4*R*(1+sin(theta)),H-2.8*R-4*R*cos(theta)))
larm=Line((4*R,H-2.8*R),(4*R*(1-sin(theta)),H-2.8*R-4*R*cos(theta)))

legs = Composition({'lleg': lleg, 'rleg': rleg})
arms = Composition({'rarm': rarm, 'larm': larm})
body = Composition({'head': head, 'torso': torso})
fig = Composition({'body': body, 'legs': legs, 'arms':arms})

fig.draw()  # send all figures to plotting backend

drawing_tool.display()
#input()
drawing_tool.savefig('ej9.20.png')
drawing_tool.savefig('ej9.20.pdf')



