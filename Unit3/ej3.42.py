genome="ACGGTTACGGAACG"
subs="GGT"

def count_substr(dna, substr):
    e1 = substr[0]
    s=0
    for i in range(len(dna)-len(substr)+1): #To ensure the substring will fit in what's left of the original string.
        if dna[i]==e1:
            s+=(dna[i:i+len(substr)]==substr)            
    return s

print count_substr(genome, subs)
