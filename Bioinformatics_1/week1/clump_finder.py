from frequent_words import frequentWords
from collections import defaultdict

def clump_finder(genome: str, k : int, L: int, t: int):
    """
     returns k-mers that form a (L,t)-clumps in a given genome
    """
    kmer_index = defaultdict(list)
    output = set()
    for i in range(len(genome)-L + 1):
        pos = genome[i:i+k]
        kmer_index[pos].append(i)
        if len(kmer_index[pos]) >= t:
            if ((kmer_index[pos][-1]+ (k-1)) - kmer_index[pos][-t]) < L:
                output.add(pos)
    return output




# finding 9-mers forming (500,3) clumps in E.coli gene
file_path = './E_coli.txt'

with open(file_path) as f:
    data = f.read()
    print(len(clump_finder(data, 9, 500, 3)))
