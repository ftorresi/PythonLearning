###8.1.5
##Evaluate mean and standard deviation
#import sys
#N = int(sys.argv[1])
#import random
#from math import sqrt
#sm = 0; sv = 0
#for q in range(1, N+1):
    #x = random.uniform(-1, 1)
    #sm += x
    #sv += x**2
    ## Write out mean and st.dev. 10 times in this loop
    #if q % int(N/10) == 0:
        #xm = sm/q
        #xs = sqrt(sv/q - xm**2)
        #print ("%10d mean: %12.5e stdev: %12.5e" % (q, xm, xs))
        
##Vectorized version
#import sys
#N = int(sys.argv[1])
#import numpy as np
#x = np.random.uniform(-1, 1, size=N)
#xm = np.mean(x)
#xv = np.var(x)
#xs = np.std(x)
#print ('%10d mean: %12.5e stdev: %12.5e' % (N, xm, xs))



###8.1.6
##Gaussian distribution
#import sys
#N = int(sys.argv[1])
#m = float(sys.argv[2])
#s = float(sys.argv[3])
#import numpy as np
#np.random.seed(12)
#samples = np.random.normal(m, s, N)
#print (np.mean(samples), np.std(samples))



###8.2.2
##Throwing a dice
#import random
#def six_eyes(N):
    #M = 0 # no of times we get 6 eyes
    #for i in range(N):
        #outcome = random.randint(1, 6)
        #if outcome == 6:
            #M += 1
    #return float(M)/N

#import numpy as np
#def six_eyes_vec(N):
    #eyes = np.random.randint(1, 7, N)
    #success = eyes == 6 # True/False array
    #M = np.sum(success) # treats True as 1, False as 0
    #return float(M)/N

#print(six_eyes(100000), six_eyes_vec(100000))

#def six_eyes_vec2(N, arraysize=10000):
    ## Split all experiments into batches of size arraysize,
    ## plus a final batch of size rest
    ## (note: N//arraysize is integer division)
    #rest = N % arraysize
    #batch_sizes = [arraysize]*(N//arraysize) + [rest] #list of (N//arraysize) elements that are arraysize, plus a last element rest
    #M = 0
    #for batch_size in batch_sizes:
        #eyes = np.random.randint(1, 7, batch_size)
        #success = eyes == 6 # True/False array
        #M += np.sum(success) # treats True as 1, False as 0
    #return float(M)/N
#print(six_eyes_vec2(1000000))

#def test_all():
    ## Use np.random as random number generator for all three
    ## functions and make sure all of them applies the same seed
    #N = 100
    #arraysize = 40
    #random.randint = lambda a, b: np.random.randint(a, b+1, 1)[0]
    #tol = 1E-15
    
    #np.random.seed(3)
    #f_scalar = six_eyes(N)
    #np.random.seed(3)
    #f_vec = six_eyes_vec(N)
    #assert abs(f_scalar - f_vec) < tol
    
    #np.random.seed(3)
    #f_vec2 = six_eyes_vec2(N, arraysize=80)
    #assert abs(f_vec - f_vec2) < tol
#test_all()


###8.2.5
##Deck as a class

#import random
##random.seed(10)

#class Deck:
    #def __init__(self):
        #ranks = ['A', '2', '3', '4', '5', '6', '7',
                 #'8', '9', '10', 'J', 'Q', 'K']
        #suits = ['C', 'D', 'H', 'S']
        #self.deck = [s+r for s in suits for r in ranks]
        #random.shuffle(self.deck)

    #def hand(self, n=1):
        #"""Deal n cards. Return hand as list."""
        #hand = [self.deck[i] for i in range(n)]  # pick cards
        #del self.deck[:n]                        # remove cards
        #return hand

    #def deal(self, cards_per_hand, no_of_players):
        #"""Deal no_of_players hands. Return list of lists."""
        #return [self.hand(cards_per_hand) for i in range(no_of_players)]

    #def putback(self, card):
        #"""Put back a card under the rest."""
        #self.deck.append(card)

    #def __str__(self):
        #return str(self.deck)
    
    
#def same_rank(hand, n_of_a_kind):
    #"""
    #Given a hand of cards, return the number of
    #n_of_a_kind combinations of ranks.
    #For example, with n_of_a_kind=2, the function
    #returns the number of pairs in the hand.
    #"""
    #ranks = [card[1:] for card in hand]
    #counter = 0
    #already_counted = []
    #for rank in ranks:
        #if rank not in already_counted and \
               #ranks.count(rank) == n_of_a_kind:
            #counter += 1
            #already_counted.append(rank)
    #return counter

#def same_suit(hand):
    #"""
    #Given a hand of cards, return the number of
    #cards of the same suit, counter[suit], for each
    #of the suits in the hand.
    #"""
    #suits = [card[0] for card in hand]
    #counter = {}   # counter[suit] = how many cards of suit
    #for suit in suits:
        ## Attention only to count > 1:
        #count = suits.count(suit)
        #if count > 1:
            #counter[suit] = count
    #return counter

#if __name__ == '__main__':
    #deck = Deck()
    #print (deck)
    #players = deck.deal(5, 4)
    #import pprint
    #pprint.pprint(players)
    #for hand in players:
        #print ("""The hand %s\nhas %d pairs, %s 3-of-a-kind and\n%s cards of the same suit.""" %(', '.join(hand), same_rank(hand, 2),same_rank(hand, 3),'+'.join([str(s) for s in same_suit(hand).values()])))
        
##Deck as a class, but now with classes Card and Hand
#import random
##random.seed(10)

#class Card:
    #"""Representation of a card as a string (suit+rank)."""
    #def __init__(self, suit, rank):
        #self.card = suit + str(rank)

    #def __str__(self):   return self.card
    #def __repr__(self):  return str(self)

#class Hand:
    #"""Representation of a hand as a list of Card objects."""
    #def __init__(self, list_of_cards):
        #self.hand = list_of_cards

    #def __str__(self):   return str(self.hand)
    #def __repr__(self):  return str(self)


#class Deck:
    #"""Representation of a deck as a list of Card objects."""

    #def __init__(self):
        #ranks = ['A', '2', '3', '4', '5', '6', '7',
                 #'8', '9', '10', 'J', 'Q', 'K']
        #suits = ['C', 'D', 'H', 'S']
        #self.deck = [Card(s,r) for s in suits for r in ranks]
        #random.shuffle(self.deck)

    #def hand(self, n=1):
        #"""Deal n cards. Return hand as a Hand object."""
        #hand = Hand([self.deck[i] for i in range(n)])
        #del self.deck[:n]         # remove cards
        #return hand

    #def deal(self, cards_per_hand, no_of_players):
        #"""Deal no_of_players hands. Return list of Hand obj."""
        #return [self.hand(cards_per_hand) for i in range(no_of_players)]

    #def putback(self, card):
        #"""Put back a card under the rest."""
        #self.deck.append(card)

    #def __str__(self):
        #return str(self.deck)

    #def __repr__(self):
        #return str(self)

    #def __len__(self):
        #return len(self.deck)

#def demo():
    #deck = Deck()
    #print( deck)
    #players = deck.deal(5, 4)
    #import pprint; pprint.pprint(players)

#if  __name__ == '__main__':
    #demo()


###8.3.4
##DNA mutation via Markov chain

#import random
#import numpy as np
#def create_markov_chain():
    #markov_chain = {}
    #for from_base in 'ATGC':
        ## Generate random transition probabilities by dividing
        ## [0,1] into four intervals of random length
       #slice_points = sorted(
           #[0] + [random.random()for i in range(3)] + [1])
       #transition_probabilities = \
           #[slice_points[i+1] - slice_points[i] for i in range(4)]
       #markov_chain[from_base] = {base: p for base, p
                         #in zip('ATGC', transition_probabilities)}
    #return markov_chain

##mc = create_markov_chain()
##print (mc)
##print (mc['A']['T']) # probability of transition from A to T

#def check_transition_probabilities(markov_chain):
    #for from_base in 'ATGC':
        #s = sum(markov_chain[from_base][to_base]
                #for to_base in 'ATGC')
        #if abs(s - 1) > 1E-15:
            #raise ValueError('Wrong sum: %s for "%s"' % \
                             #(s, from_base))

##check_transition_probabilities(mc)

#def draw(discrete_probdist):
    #"""
    #Draw random value from discrete probability distribution
    #represented as a dict: P(x=value) = discrete_probdist[value].
    #"""
    ## Method:
    ## http://en.wikipedia.org/wiki/Pseudo-random_number_sampling
    #limit = 0
    #r = random.random()
    #for value in discrete_probdist:
        #limit += discrete_probdist[value]
        #if r < limit:
            #return value

#def draw_vec(discrete_probdist, N):
    #"""Vectorized version of draw."""
    #limit = 0
    #r = np.random.random(N)
    #counter = {}
    #for value in discrete_probdist:
        #limit += discrete_probdist[value]
        #counter[value] = np.sum(r < limit)
        #r = r[r >= limit]
    #s = []
    #for value in counter:
        #a = np.zeros(counter[value], dtype=type(value))
        #a[:] = value
        #s.append(a)
    #values = np.concatenate(s)
    #np.random.shuffle(values)
    #return values

#def check_draw_approx(discrete_probdist, N=1000000):
    #"""
    #See if draw results in frequencies approx equal to
    #the probability distribution.
    #"""
    #frequencies = {value: 0 for value in discrete_probdist}
    #for i in range(N):
        #value = draw(discrete_probdist)
        #frequencies[value] += 1
    #for value in frequencies:
        #frequencies[value] /= float(N)
    #print (', '.join(['%s: %.4f (exact %.4f)' % \
                     #(v, frequencies[v], discrete_probdist[v])
                     #for v in frequencies]))

#def check_draw_vec_approx(discrete_probdist, N=1000000):
    #"""
    #See if draw_vec results in frequencies approx equal to
    #the probability distribution.
    #"""
    #frequencies = {value: 0 for value in discrete_probdist}
    #values = draw_vec(discrete_probdist, N)
    #lst = values.tolist()
    #for value in frequencies:
        #frequencies[value] += lst.count(value)
    #for value in frequencies:
        #frequencies[value] /= float(N)
    #print (', '.join(['%s: %.4f (exact %.4f)' % \
                     #(v, frequencies[v], discrete_probdist[v])
                     #for v in frequencies]))

##check_draw_approx(mc['A'])
##check_draw_vec_approx(mc['A'])
##for i in range(4):
    ##print ('A to', draw(mc['A']))
    
#def mutate_via_markov_chain(dna, markov_chain):
    #dna_list = list(dna)
    #mutation_site = random.randint(0, len(dna_list) - 1)
    #from_base = dna[mutation_site]
    #to_base = draw(markov_chain[from_base])
    #dna_list[mutation_site] = to_base
    #return ''.join(dna_list)

##From unit 6, function to compute bases frequencies
#def get_base_frequencies_v2(dna):
        #return {base: dna.count(base)/float(len(dna))
                #for base in 'ATGC'}
    
#def format_frequencies(frequencies):
    #return ', '.join(['%s: %.2f' % (base, frequencies[base])
                      #for base in frequencies])

#dna = 'TTACGGAGATTTCGGTATGCAT'
#print ('Starting DNA:', dna)
#print (format_frequencies(get_base_frequencies_v2(dna)))

#mc = create_markov_chain()
#import pprint
#print ('Transition probabilities:\n', pprint.pformat(mc))
#nmutations = 10000
#for i in range(nmutations):
    #dna = mutate_via_markov_chain(dna, mc)

#print ('DNA after %d mutations (Markov chain):' % nmutations, dna)
#print (format_frequencies(get_base_frequencies_v2(dna)))



####8.3.5
###Birth Control policies

#import random
#import numpy as np

#MALE = 1;  FEMALE = 2

#def get_children(n, male_portion, fertility):
    #if n == 0: return []
    #n = int(fertility*n)  # not all n couples get a child
    #r = np.random.random(n)
    #children = np.zeros(n, int)
    #children[r <  male_portion] = MALE
    #children[r >= male_portion] = FEMALE
    #return children
    
#def advance_generation(parents, policy='one child',
                       #male_portion=0.5, fertility=1.0,
                       #law_breakers=0, wanted_children=4):
    #"""
    #Given a generation of parents (random integers with
    #values MALE or FEMALE), compute the next generation
    #of children.
    #Return: array of children (MALE and FEMALE values),
    #and the maximum number of children found in a family.
    #"""
    #males = len(parents[parents==MALE])
    #females = len(parents) - males
    #couples = min(males, females)

    #if policy == 'one child':
        ## Each couple gets one child.
        #children = get_children(couples, male_portion, fertility)
        #max_children = 1
    #elif policy == 'one son':
        ## Each couple can continue with a new child until 
        ## they get a son.

        ## First try.
        #children = get_children(couples, male_portion, fertility)
        #max_children = 1
        ## Continue with getting a new child for each daughter.
        #daughters = children[children == FEMALE]
        #while len(daughters) > 0:
            #new_children = get_children(len(daughters),
                                        #male_portion, fertility)
            #children = np.concatenate((children, new_children))
            #daughters = new_children[new_children == FEMALE]
            #max_children += 1
    ## A portion law_breakers breaks the law and gets wanted_children.
    #illegals = get_children(int(len(children)*law_breakers)*wanted_children,
                            #male_portion, fertility=1.0)
    #children = np.concatenate((children, illegals))
    #return children, max_children

#N = 1000000
#male_portion = 0.51
#fertility = 0.92
#law_breakers = 0.06
#wanted_children = 5

#generations = 10
## Start with a "perfect" generation of parents.
#start_parents = get_children(N, male_portion=0.5, fertility=1.0)
#parents = start_parents.copy()
#print ('one child policy, start: %d' % len(parents))
#for i in range(generations):
    #parents, mc = advance_generation(parents, 'one child',
                                     #male_portion, fertility,
                                     #law_breakers, wanted_children)
    #print ('%3d: %d' % (i+1, len(parents)))

#parents = start_parents.copy()
#print ('one son policy, start: %d' % len(parents))
#for i in range(generations):
    #parents, mc = advance_generation(parents, 'one son',
                                     #male_portion, fertility,
                                     #law_breakers, wanted_children)
    #print ('%3d: %d (max children in a family: %d)' % \
          #(i+1, len(parents), mc))



####8.6.2
###Random Walk 1D with visualization

#import matplotlib.pyplot as plt
#import time, sys
#import random, numpy

#try:
    #np = int(sys.argv[1])
    #ns = int(sys.argv[2])
#except IndexError:
    #np = 4     # no of particles
    #ns = 100   # no of steps


#xmax = numpy.sqrt(ns); xmin = -xmax    # initial extent of plot axis
#positions = numpy.zeros(np)            # all particles start at x=0
#HEAD = 1;  TAIL = 2                    # constants

#y = positions.copy()                   # y position is always 0
#y0=[el+0.01 for el in y]

#for step in range(ns):
    #for p in range(np):
        #coin = random.randint(1,2)     # flip coin
        #if coin == HEAD:
            #positions[p] += 1   # one unit length to the right
        #elif coin == TAIL:
            #positions[p] -= 1   # one unit length to the left

    #if min(positions) < xmin:  xmin -= 2*numpy.sqrt(ns)
    #if max(positions) > xmax:  xmax += 2*numpy.sqrt(ns)
    #y=y+y0 #On each step, move sligthly up so we have a "time" axis on y
    #plt.axis([xmin, xmax, 0, 0.01*(ns+2)])
    #plt.plot(positions, y, 'ko:',markersize=3) 
    ##time.sleep(0.2)             # pause before next move
    ## Extend x axis limits?

#plt.show()


####8.6.5
#"""
#Vectorized implementation of walk1Dp.py/walk1Ds.py,
#but without graphics (for efficiency).
#"""
#import numpy  # not as np since np is an important variable here
#import time, sys

#numpy.random.seed(11)

#try:
    #np = int(sys.argv[1])  # number of particles
    #ns = int(sys.argv[2])  # number of steps
#except IndexError:
    #np = 2000
    #ns = 200

## Draw from 1, 2
#moves = numpy.random.random_integers(1, 2, size=np*ns)
## Transform 1 to -1 and 2 to 1
#moves = 2*moves - 3
#moves.shape = (ns, np)

#positions = numpy.zeros(np)
#for step in range(ns):
    #positions += moves[step, :]
    
    #mean_pos = numpy.mean(positions)
    #stdev_pos = numpy.std(positions)
    #print (mean_pos, stdev_pos)


def random_walk_2D(np, ns):
    xpositions = numpy.zeros(np)
    ypositions = numpy.zeros(np)

    NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4  # constants

    for step in range(ns):
        print(xpositions, ypositions)
        for i in range(np):
            direction = random.randint(1, 4)
            if direction == NORTH:
                ypositions[i] += 1
            elif direction == SOUTH:
                ypositions[i] -= 1
            elif direction == EAST:
                xpositions[i] += 1
            elif direction == WEST:
                xpositions[i] -= 1
    return xpositions, ypositions

# main program:
import random
random.seed(10)
import sys
import numpy

np        = int(sys.argv[1])  # number of particles
ns        = int(sys.argv[2])  # number of steps
x,y=random_walk_2D(np, ns)











#"""
#Is x*x more efficient than x**2 for a large array x?
#This program applies the timeit module to investigate this
#question.
#"""
#import timeit
#n = 1000000  # length of array

#initcode = """
#from numpy import zeros
#from __main__ import n
#x = zeros(n)
#"""

#nrep = 80  # repeat x*x and x**2 nrep times

#t = timeit.Timer('x*x', setup=initcode)
#t1 = t.timeit(nrep)
#t = timeit.Timer('x**2', setup=initcode)
#t2 = t.timeit(nrep)
#print ('x**2 vs x*x for arrays of length %d:' % n, t2/t1)
#print ('x*x is %g times faster than x**2 for such arrays' % (t2/t1))
## Repeat the test for math.pow and ** for scalars

#nrep = 8000000

#t = timeit.Timer('2.0*2.0')
#t1 = t.timeit(nrep)
#t = timeit.Timer('2.0**2')
#t2 = t.timeit(nrep)
#print ('2.0**2 vs 2.0*2.0:', t2/t1)
#t = timeit.Timer('2.0**2.0')
#t2 = t.timeit(nrep)
#print ('2.0**2.0 vs 2.0*2.0:', t2/t1)
#t = timeit.Timer('pow(2.0,2)', setup='from math import pow')
#t2 = t.timeit(nrep)
#print ('pow(2.0,2) vs 2.0*2.0:', t2/t1)


