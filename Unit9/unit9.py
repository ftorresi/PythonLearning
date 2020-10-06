###moving car

#from pysketcher import *

#R = 1    # radius of wheel
#L = 4    # distance between wheels
#H = 2    # height of vehicle body
#w_1 = 5  # position of front wheel

#xmax = w_1 + 2*L + 3*R
#drawing_tool.set_coordinate_system(xmin=0, xmax=xmax,
                                   #ymin=-1, ymax=2*R + 3*H,
                                   #axis=False)

#wheel1 = Circle(center=(w_1, R), radius=R)
#wheel2 = wheel1.copy()
#wheel2.translate((L,0))

#under = Rectangle(lower_left_corner=(w_1-2*R, 2*R),
                  #width=2*R + L + 2*R, height=H)
#over  = Rectangle(lower_left_corner=(w_1, 2*R + H),
                  #width=2.5*R, height=1.25*H)

#wheels = Composition({'wheel1': wheel1, 'wheel2': wheel2})
#body = Composition({'under': under, 'over': over})

#vehicle = Composition({'wheels': wheels, 'body': body})
#ground = Wall(x=[R, xmax], y=[0, 0], thickness=-0.3*R)

#fig = Composition({'vehicle': vehicle, 'ground': ground})
#fig.draw()  # send all figures to plotting backend

#drawing_tool.display()
#drawing_tool.savefig('tmp1.png')
#drawing_tool.savefig('tmp1.pdf')

#fig['vehicle']['wheels'].set_filled_curves('blue')
#fig['vehicle']['wheels'].set_linewidth(6)
#fig['vehicle']['wheels'].set_linecolor('black')
#fig['vehicle']['body']['under'].set_filled_curves('red')
#fig['vehicle']['body']['over'].set_filled_curves(pattern='/')
#fig['vehicle']['body']['over'].set_linewidth(14)

#drawing_tool.erase()  # avoid drawing old and new fig on top of each other
#fig.draw()
#drawing_tool.display()
#drawing_tool.savefig('tmp2.png')
#drawing_tool.savefig('tmp2.pdf')

##print (fig)
##fig.recurse('fig')
##fig.graphviz_dot('fig', False)

#import time
#time.sleep(1)

## Animate motion
#fig['vehicle'].translate((L,0))  # move to start point for "driving"

#def v(t):
    #return -8*R*t*(1 - t/(2*R))

#import numpy
#tp = numpy.linspace(0, 2*R, 25)
#dt = tp[1] - tp[0]  # time step

#def move(t, fig):
    #x_displacement = dt*v(t)
    #fig['vehicle'].translate((x_displacement, 0))

#files = animate(fig, tp, move, moviefiles=True,
                #pause_per_frame=0)

#files_wildcard = files.split('%')[0] + '*.png'
#os.system('convert -delay 20 %s* vehicle0.gif' % (files_wildcard))


###moving car with rotating wheels
from pysketcher import *

R = 1    # radius of wheel
L = 4    # distance between wheels
H = 2    # height of vehicle body
w_1 = 5  # position of front wheel

xmax = w_1 + 2*L + 3*R
drawing_tool.set_coordinate_system(xmin=0, xmax=xmax,
                                   ymin=-1, ymax=2*R + 3*H,
                                   axis=False)

wheel1 = Composition({
    'wheel': Circle(center=(w_1, R), radius=R),
    'cross': Composition({'cross1': Line((w_1,0),   (w_1,2*R)),
                          'cross2': Line((w_1-R,R), (w_1+R,R))})})
wheel2 = wheel1.copy()
wheel2.translate((L,0))

under = Rectangle(lower_left_corner=(w_1-2*R, 2*R),
                  width=2*R + L + 2*R, height=H)
over  = Rectangle(lower_left_corner=(w_1, 2*R + H),
                  width=2.5*R, height=1.25*H)

wheels = Composition({'wheel1': wheel1, 'wheel2': wheel2})
body = Composition({'under': under, 'over': over})

vehicle = Composition({'wheels': wheels, 'body': body})
ground = Wall(x=[R, xmax], y=[0, 0], thickness=-0.3*R)

fig = Composition({'vehicle': vehicle, 'ground': ground})
fig.draw()  # send all figures to plotting backend

drawing_tool.display()
drawing_tool.savefig('tmp1.png')
drawing_tool.savefig('tmp1.pdf')

#print (fig)

import time
time.sleep(1)
from math import degrees

# Animate motion
w_1 += L                         # start position
fig['vehicle'].translate((L,0))  # move whole figure to start position

def v(t):
    return -8*R*t*(1 - t/(2*R))

import numpy
tp = numpy.linspace(0, 2*R, 25)
dt = tp[1] - tp[0]  # time step

def move(t, fig):
    x_displacement = dt*v(t)
    fig['vehicle'].translate((x_displacement, 0))

    # Rotate wheels
    global w_1
    w_1 += x_displacement
    # R*angle = -x_displacement
    angle = - x_displacement/R
    w1 = fig['vehicle']['wheels']['wheel1']
    w1.rotate(degrees(angle), center=(w_1, R))
    w2 = fig['vehicle']['wheels']['wheel2']
    w2.rotate(degrees(angle), center=(w_1 + L, R))

files = animate(fig, tp, move, moviefiles=True,
                pause_per_frame=0)

files_wildcard = files.split('%')[0] + '*.png'
os.system('convert -delay 20 %s* vehicle1.gif' % (files_wildcard))

