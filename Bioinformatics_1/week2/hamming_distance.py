import sys

def hamming_distance(kmer_1 , kmer_2):
    """
     hamming_distance calculates the mismatch between two kmers
     params:
     kmer_1(str): The first kmer
     kmer_2(str): The second kmer
     Returns:
     hamming_distance(int): This is the number of mismatches between two strings
    """
    long = ""
    short = ""

    if len(kmer_1) > len(kmer_2):
        long = kmer_1
        short = kmer_2
    else:
        long = kmer_2
        short = kmer_1

    diff = [1 for index in range(
        len(short)) if long[index] != short[index]]
    hamming_distance = sum(diff)
    temp = len(long) - len(short)
    hamming_distance = hamming_distance + temp
    return hamming_distance


list_1 = sys.argv[1]
list_2 = sys.argv[2]
print(list_1)

x = hamming_distance(list_1, list_2)
print("hamming distance", x)
