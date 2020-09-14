##8.3.4
#DNA mutation via Markov chain

import random, time
import numpy as np
def create_markov_chain():
    markov_chain = {}
    for from_base in 'ATGC':
        # Generate random transition probabilities by dividing
        # [0,1] into four intervals of random length
       slice_points = sorted(
           [0] + [random.random()for i in range(3)] + [1])
       transition_probabilities =  [slice_points[i+1] - slice_points[i] for i in range(4)]
       markov_chain[from_base] = {base: p for base, p
                         in zip('ATGC', transition_probabilities)}
    return markov_chain

def check_transition_probabilities(markov_chain):
    for from_base in 'ATGC':
        s = sum(markov_chain[from_base][to_base]
                for to_base in 'ATGC')
        if abs(s - 1) > 1E-15:
            raise ValueError('Wrong sum: %s for "%s"' % \
                             (s, from_base))


def draw(discrete_probdist):
    """
    Draw random value from discrete probability distribution
    represented as a dict: P(x=value) = discrete_probdist[value].
    """
    # Method:
    # http://en.wikipedia.org/wiki/Pseudo-random_number_sampling
    limit = 0
    r = random.random()
    for value in discrete_probdist:
        limit += discrete_probdist[value]
        if r < limit:
            return value

def draw_vec(discrete_probdist, N):
    """Vectorized version of draw."""
    limit = 0
    r = np.random.random(N)
    counter = {}
    for value in discrete_probdist:
        limit += discrete_probdist[value]
        counter[value] = np.sum(r < limit)
        r = r[r >= limit]
    s = []
    for value in counter:
        a = np.zeros(counter[value], dtype=type(value))
        a[:] = value
        s.append(a)
    values = np.concatenate(s)
    np.random.shuffle(values)
    return values

def check_draw_approx(discrete_probdist, N=1000000):
    """
    See if draw results in frequencies approx equal to
    the probability distribution.
    """
    frequencies = {value: 0 for value in discrete_probdist}
    for i in range(N):
        value = draw(discrete_probdist)
        frequencies[value] += 1
    for value in frequencies:
        frequencies[value] /= float(N)
    print (', '.join(['%s: %.4f (exact %.4f)' % \
                     (v, frequencies[v], discrete_probdist[v])
                     for v in frequencies]))

def check_draw_vec_approx(discrete_probdist, N=1000000):
    """
    See if draw_vec results in frequencies approx equal to
    the probability distribution.
    """
    frequencies = {value: 0 for value in discrete_probdist}
    values = draw_vec(discrete_probdist, N)
    lst = values.tolist()
    for value in frequencies:
        frequencies[value] += lst.count(value)
    for value in frequencies:
        frequencies[value] /= float(N)
    print (', '.join(['%s: %.4f (exact %.4f)' % \
                     (v, frequencies[v], discrete_probdist[v])
                     for v in frequencies]))

#mc = create_markov_chain()
#check_draw_approx(mc['A'])
#check_draw_vec_approx(mc['A'])
    
def mutate_via_markov_chain(dna, markov_chain):
    dna_list = list(dna)
    mutation_site = random.randint(0, len(dna_list) - 1)
    from_base = dna[mutation_site]
    to_base = draw(markov_chain[from_base])
    dna_list[mutation_site] = to_base
    return ''.join(dna_list)

#From unit 6, function to compute bases frequencies
def get_base_frequencies_v2(dna):
        return {base: dna.count(base)/float(len(dna))
                for base in 'ATGC'}
    
def format_frequencies(frequencies):
    return ', '.join(['%s: %.2f' % (base, frequencies[base])
                      for base in frequencies])

t0=time.clock()
dna = 'TTACGGAGATTTCGGTATGCAT'
#print ('Starting DNA:', dna)
#print (format_frequencies(get_base_frequencies_v2(dna)))

mc = create_markov_chain()
import pprint
#print ('Transition probabilities:\n', pprint.pformat(mc))
nmutations = 1000000
for i in range(nmutations):
    dna = mutate_via_markov_chain(dna, mc)

#print ('DNA after %d mutations (Markov chain):' % nmutations, dna)
#print (format_frequencies(get_base_frequencies_v2(dna)))
t1=time.clock()

###Functions chaged according to exercise (I guess...)

def createlimits(discrete_probdist):
    #Evaluate limits for a Markov Chain
    limits={}
    for from_base in 'ATGC':
        l=0
        limits[from_base]={}
        for to_base in 'ATGC':
            l+=discrete_probdist[from_base][to_base]
            limits[from_base][to_base]=l
    return limits

def draw2(limits):
    #Same as draw but using limits created with createlimits
    r = random.random()
    for value in limits:
        if r < limits[value]:
            return value

def mutate_via_markov_chain2(dna, lim):
    #Same as mutate_via_markov_chain2 but using draw2
    dna_list = list(dna)
    mutation_site = random.randint(0, len(dna_list) - 1)
    from_base = dna[mutation_site]
    to_base = draw2(lim[from_base])
    dna_list[mutation_site] = to_base
    return ''.join(dna_list)


        
        
dna = 'TTACGGAGATTTCGGTATGCAT'
#print ('Starting DNA:', dna)
#print (format_frequencies(get_base_frequencies_v2(dna)))

mc = create_markov_chain()
lim=createlimits(mc) #Create Markov Chain Limits for draw
import pprint
#print ('Transition probabilities:\n', pprint.pformat(mc))
nmutations = 1000000
for i in range(nmutations):
    dna = mutate_via_markov_chain2(dna, lim)

#print ('DNA after %d mutations (Markov chain):' % nmutations, dna)
#print (format_frequencies(get_base_frequencies_v2(dna)))
t2=time.clock()


print("After %d mutations:"%nmutations)
print("Original time:",(t1-t0))
print("New time:",(t2-t1))
print("Rate Original time/New time:",((t1-t0)/(t2-t1)))
print("Doesn't look like a great improvement... :(") 
