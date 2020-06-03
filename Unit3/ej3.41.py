genome="ACTGCTATCCATTT"
par="TA"

def count_pairs(dna, pair):
    e1, e2= pair
    s=0
    for i in range(len(dna)-1): #Last letter doesn't matter 
      s+=(dna[i]==e1 and dna[i+1]==e2) #adds 1 if pair appears on position i,i+1
    return s

print count_pairs(genome, par)
