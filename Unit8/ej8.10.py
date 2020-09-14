import random
def throw_dice():
    d=random.randint(1, 6)
    return d

def compute_prob(N=None,d=None,s=None):
    if N==None:
        N = int(input('How many experiments? '))
    if d==None:
        d = int(input('How many dice? '))
    if s==None:
        s = int(input('Limit sum? '))
    w=0 #number of winnings
    for i in range(N):
        total=0
        for j in range(d):
            total+=throw_dice()
        if total<s:w+=1 
    p=w/N
    return p
    #print("Probability of getting a sum less than %i when rolling %i dice: %g" %(s, d, p))

def test_compute_prob():
    Nt=100000 #experiments
    dt=3 #3 dice
    prob=compute_prob(Nt,dt,2) #should be 0
    assert prob==0, "Prob. isn't 0 when it should" 
    prob=compute_prob(Nt,dt,20) #should be 1
    assert prob==1, "Prob. isn't 1 when it should"
    
    random.seed(10) #got numbers 5 1 4 4 5 1 2 4 on eight dice throws (sum 6 8 6 6 on each pair of dice)
    Nt=4 #experiments
    dt=2 #2 dice
    ss=7 #Should be less than 7 with p=0.75
    prob=compute_prob(Nt,dt,ss) #should be 0.75
    assert abs(prob-0.75)<1e-14, "Prob. isn't 0.75 when it should"
    
    
test_compute_prob()
