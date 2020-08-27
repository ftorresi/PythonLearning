import numpy as np

class Vec:
    def __init__(self, *args):
        if len(args)==1: #components given as list, tuple or array, args is a tuple of a tuple/list/array
            self.components=np.asarray(args[0], float)
        else: #components given individually, args is a tuple of components
            self.components=np.asarray(args, float)
            
    def __str__(self):
        s='('
        for c in self.components[:-1]:
            s+='%g, ' %c
        s+='%g)' %self.components[-1]
        return s
    
    def __add__(self, other):
        if isinstance(other, (list,tuple,np.ndarray)):
            other = Vec(other)
        elif not (len(self.components)==len(other.components)):
            raise TypeError('vectors to sum must have the same dimension')
        return Vec(self.components+other.components)
    
    def __radd__(self, other):
        print(other, type(other))
        print(self, type(self))
        return self.__add__(other)
    
    
    def __sub__(self, other):
        if isinstance(other, (list,tuple,np.ndarray)):
            other = Vec(other)
        elif not (len(self.components)==len(other.components)):
            raise TypeError('vectors to sum must have the same dimension')
        return Vec(self.components-other.components) 
    
    def __rsub__(self, other):
        if isinstance(other, (list,tuple,np.ndarray)):  #make other a Vec2D object in order to use other.__sub__
            other = Vec(other)                          #since __sub__ is not defined for list/tuple
        elif not (len(self.components)==len(other.components)):
            raise TypeError('vectors to sum must have the same dimension')              
        return other.__sub__(self)
    
    def __mul__(self, other):              
        return sum((self.components*other.components))
    
    def __abs__(self):
        return np.sqrt(self.__mul__(self))
    
    def __eq__(self, other):
        return (self.components == other.components).all()
    
    def __ne__(self, other):
        return not self.__eq__(other) # reuse __eq__

        
##Some tests

#v= Vec(1, -1)
#print (v)
#a= np.array([1, -1, 4], float)
#v= Vec(a)
#print (v)
#v= Vec([1, -1, 4])
#print (v)
#v= Vec((1, -1, 4))
#print (v)

#print(v+v)
#print(v+a) #vec+array
#print(v+[1, -1, 4]) #vec+list
#print(v+(1, -1, 4)) #vec+tuple

#print([1, -1, 4]+v) #list+vec
#print((1, -1, 4)+v) #tuple+vec
#b=np.array([2, -1, 4], float)
##print(b, type(b))
##print (b+v) #vec+array      #BUG NOT WORKING
#print (v.__radd__(b))    #works fine

#print(v-v)
#print(v-np.array([1, -1, 5], float)) #vec-array
#print(v-[1, -1, 5]) #vec-list
#print(v-(1, -1, 5)) #vec-tuple


#print([1, -1, 5]-v) #list-vec
#print((1, -1, 5)-v) #tuple-vec
#c=np.array([1, -1, 5], float)
##print((c-v)) #array-vec   #BUG NOT WORKING
#print (v.__rsub__(c))    #works fine


#v=Vec(2,1,-2)
#w=Vec(0,0,1)
#print (v*w)
#print(abs(v))
#print(v==w)
#print(v!=v)
#print(v!=w)




