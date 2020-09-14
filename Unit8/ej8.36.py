class Particle:
    def __init__(self,x,y,n):
       self.x, self.y=x,y
       self.n=n
       
    def move(self):
        self.n+=1 #step increased one
        direction = random.randint(1, 4)
        if direction == 1:
            self.y += 1
        elif direction == 2:
            self.y -= 1
        elif direction == 4: #to coincide w/walk2d.py
            self.x += 1
        elif direction == 3:
            self.x -= 1
            
    def __str__(self):
        return "(%5.2f;%5.2f)"%(self.x, self.y)
    
    def __repr__(self):
        return self.__str__()
    
    
    
class Particles:
    def __init__(self,np,plotstep=1):
        self.pars=[Particle(0,0,0) for i in range(np)] #list of np particles initially at (0;0)
        self.plotstep=plotstep
    
    def move(self):
        for p in self.pars:
            p.move()
    
    def plot(self):
        plt.figure()
        x=[p.x for p in self.pars] #x-list
        y=[p.y for p in self.pars] #y-list
        plt.plot(x,y,"ko")    
        
    def moves(self,ns): #move ns steps
        self.plot() #plot initial step
        plt.savefig("ej8.36_0000.png")
        for i in range(ns):
            self.move()
            if (i+1) % self.plotstep == 0: #plot every plotstep steps
                self.plot()
                num=int((i+1)/self.plotstep)
                plt.savefig("ej8.36_%04d.png" %num)
            
    def __str__(self):
        import pprint
        pp=pprint.pformat(self.pars)
        return pp
    
    def __repr__(self):
        return self.__str__()
    
    
def test_particles():
    import random
    random.seed(10)
    particles=Particles(4,1000)
    
    particles.move() #1st move
    x=[0,1,1,0]; y=[1,0,0,1] #Obtained for seed=10 in walk2d.py
    s=0
    for i in range(len(particles.pars)):
       p=particles.pars[i]
       s+=abs(p.x-x[i])+abs(p.x-x[i])
    assert s<1e-10, "Difference in 1st move"
        
    particles.move() #2nd move
    x=[0,2,2,-1]; y=[0,0,0,1] #Obtained for seed=10 in walk2d.py
    s=0
    for i in range(len(particles.pars)):
       p=particles.pars[i]
       s+=abs(p.x-x[i])+abs(p.x-x[i])
    assert s<1e-10, "Difference in 2nd move"
    
    particles.move() #3rd move
    x=[0,2,3,-2]; y=[-1,1,0,1] #Obtained for seed=10 in walk2d.py
    s=0
    for i in range(len(particles.pars)):
       p=particles.pars[i]
       s+=abs(p.x-x[i])+abs(p.x-x[i])
    assert s<1e-10, "Difference in 3rd move"
    
    
    
class Particles_vec:
    def __init__(self,np,plotstep):
        self.np=np
        self.x = numpy.zeros(np)
        self.y = numpy.zeros(np)
        self.plotstep=plotstep
    
    def plot(self):
        plt.figure()
        #x=[p.x for p in self.pars] #x-list
        #y=[p.y for p in self.pars] #y-list
        plt.plot(self.x,self.y,"ko")    
        
    def moves(self,ns): #move ns steps
        moves = numpy.random.random_integers(1, 4, size=ns*self.np)
        moves.shape = (ns, self.np)
        self.plot() #plot initial step
        plt.savefig("ej8.36_0000.png")
        for step in range(ns):
            this_move = moves[step,:]
            self.y += numpy.where(this_move == 1, 1, 0)
            self.y -= numpy.where(this_move == 2, 1, 0)
            self.x += numpy.where(this_move == 4, 1, 0)
            self.x -= numpy.where(this_move == 3, 1, 0)
            if (step+1) % self.plotstep == 0: #plot every plotstep steps
                self.plot()
                num=int((step+1)/self.plotstep)
                plt.savefig("ej8.36_%04d.png" %num)

            
    def __str__(self):
        import pprint
        plist=[(x,y) for x,y in zip(self.x,self.y)]
        pp=pprint.pformat(plist)
        return pp
    
    def __repr__(self):
        return self.__str__()
    
    
def test_particles_vec():
    numpy.random.seed(10)
    particles=Particles_vec(4,1000)
    
    particles.moves(1) #1st move
    x=[0,0,0,1]; y=[-1,-1,1,0] #Obtained for seed=10 
    success=numpy.allclose(particles.x,x) and numpy.allclose(particles.y,y)
    assert success, "Difference in 1st move"
        
    particles.moves(1) #2nd move
    x=[0,0,1,1]; y=[0,-2,1,1] #Obtained for seed=10 
    success=numpy.allclose(particles.x,x) and numpy.allclose(particles.y,y)
    assert success, "Difference in 2nd move"
    
    particles.moves(1) #3rd move
    x=[0,0,1,1]; y=[-1,-3,2,0] #Obtained for seed=10     
    success=numpy.allclose(particles.x,x) and numpy.allclose(particles.y,y)
    assert success, "Difference in 3rd move"

    #Main program 
if __name__ == '__main__':
    import sys, numpy, random
    import matplotlib.pyplot as plt
    test_particles()
    test_particles_vec()
    try:
        np = int(sys.argv[1]) 
    except:
        np=int(input("Number of particles? "))
    
    ##Trial for scalar version
    #parts=Particles(np,1000)
    #print("Initial state:")
    #print(parts)
    #parts.moves(2000)
    #print("State after 2000 moves:")
    #print(parts)
    
    #Trial for vectorized version
    parts=Particles_vec(np,1000)
    print("Initial state:")
    print(parts)
    parts.moves(2000)
    print("State after 2000 moves:")
    print(parts)
    
    

