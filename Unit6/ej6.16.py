import pprint   # for nice printout of nested data structures
from collections import defaultdict

#Our goal is to create a find_consensus function that works for the three cases bellow 

fm1=[[0, 0, 0, 2, 0], [0, 0, 0, 0, 2], [3, 3, 0, 1, 1], [0, 0, 3, 0, 0]] #list of lists
fm2={'A': {0: 0, 1: 0, 2: 0, 3: 2, 4: 0},  'C': {0: 0, 1: 0, 2: 0, 3: 0, 4: 2},  'G': {0: 3, 1: 3, 2: 0, 3: 1, 4: 1},  'T': {0: 0, 1: 0, 2: 3, 3: 0, 4: 0}} #dict of dicts
fm3={base: defaultdict(lambda: 0) for base in 'ACGT'} #generate dict of dicts with default value 0 for non specified indices
fm3['A'][3]=2; fm3['C'][4]=2; fm3['G'][0]=3; fm3['G'][1]=3; fm3['G'][3]=1; fm3['G'][4]=1; fm3['T'][2]=3 #Enter non-zero values



def find_consensus(frequency_matrix):
    if isinstance(frequency_matrix, list) and isinstance(frequency_matrix[0], list):
        base2index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        dna_length = len(frequency_matrix[0])
    elif isinstance(frequency_matrix, dict) and isinstance(frequency_matrix['A'], dict):
        base2index = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'T'}
        
        keylist=[list(frequency_matrix[base].keys()) for base in 'ACGT'] #get a list of 4 -A,C,G,T- lists with key values
        dna_length=max(max(elem) for elem in keylist)+1 #find max in each sublist, then absolute max, and add 1 since keys start at 0.


    else:
        raise TypeError('frequency_matrix must be list of list or dict of dicts')

    consensus = ''

    for i in range(dna_length):  # loop over positions in string
        max_freq = -1            # holds the max freq. for this i
        max_freq_base = None     # holds the corresponding base

        for base in 'ACGT':
            if frequency_matrix[base2index[base]][i] > max_freq:
                max_freq = frequency_matrix[base2index[base]][i]
                max_freq_base = base
            elif frequency_matrix[base2index[base]][i] == max_freq:
                max_freq_base = '-' # more than one base as max

        consensus += max_freq_base  # add new base with max freq
    return consensus

pprint.pprint(fm1)
print( 'Consensus string:', find_consensus(fm1))

pprint.pprint(fm2)
print( 'Consensus string:', find_consensus(fm2))

pprint.pprint(fm3)
print( 'Consensus string:', find_consensus(fm3))
