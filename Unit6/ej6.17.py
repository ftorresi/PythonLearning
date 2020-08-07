import pprint   # for nice printout of nested data structures
from collections import defaultdict

def get_base_counts_acgt(dna): #assuming no other letters are needed appart from ACGT
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for base in dna:
        if base in 'ACGT':
            counts[base] += 1
    return counts


def get_base_counts_all(dna): #assuming we want to count frequency of all letters
    counts = defaultdict(lambda: 0) #dict with initial value=0 for any key
    for base in dna:
        counts[base] += 1
    return counts



dnastring="ADLSTTLLD"
countacgt=get_base_counts_acgt(dnastring)
countall=get_base_counts_all(dnastring)

print("Method 1: Keeping only 'ACGT'")
for base, count in countacgt.items():
    print (base, count)

print("Method 2: Keeping all appearing letters")    
for base, count in countall.items():
    print (base, count)

