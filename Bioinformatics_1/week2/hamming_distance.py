import os.path
import sys


def hamming_distance(string_1, string_2):
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

    if len(string_1) > len(string_2):
        long = string_1
        short = string_2
    else:
        long = string_2
        short = string_1

    diff = [1 for index in range(
        len(short)) if long[index] != short[index]]
    temp_hd = sum(diff)

    temp = len(long) - len(short)
    temp_hd = temp_hd + temp
    return temp_hd


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("[Usage]: python hamming_distance.py file.txt")
        quit()

    sequence_input = sys.argv[1]
    kmer_1 = ""
    kmer_2 = ""

    if os.path.isfile(sequence_input) and os.path.exists(sequence_input):
        with open(sequence_input) as f:
            kmer_1 = f.readline()
            kmer_2 = f.readline()
    else:
        print(f"File {sequence_input} does not exist")
        quit()

    hd = hamming_distance(kmer_1, kmer_2)
    print(f"hamming distance between the two sequences is {hd}")
