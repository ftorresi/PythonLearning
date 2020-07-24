import numpy as np
x = np.linspace(0, 2, 1000)
y = np.cos(18*np.pi*x)
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()

#using y=cos(18*pi*x) (with pi and cos imported from math) results in an error since math functions do not work with arrays. 
#in addition, we have to increase the number of points to use in the plot to see all the oscilations in the function.
