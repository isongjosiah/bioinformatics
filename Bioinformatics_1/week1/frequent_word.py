""" Frequent word

This module allows the user determine the frequent k-mer in any genomic sequence
"""
from os import sys
from pattern_count import pattern_count

def frequent_words(genome: str, k: int):
    frequent_patterns = set()

    length: int = len(genome) - k + 1
    count: list = []
    for i in range(length):
        pattern =  genome[i:i+k]
        count.insert(i,  pattern_count(genome, pattern))
    print("count", count)
    max_count = max(count)
    for i in range(length):
        val = count[i]
        if val == max_count:
            frequent_patterns.add(genome[i:i+k])
    return frequent_patterns

if __name__ == "__main__":
    genome_pattern = sys.argv[1]
    k = int(sys.argv[2])
    print(f"The frequent {k}-mer pattern in the genomic sequence are {frequent_words(genome_pattern, k)}")
