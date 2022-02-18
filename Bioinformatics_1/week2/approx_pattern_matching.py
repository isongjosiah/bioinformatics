import os.path
import sys

from hamming_distance import hamming_distance


def approximate_pattern_matching(sequence: str, kmer_pattern: str, tolerance: int) -> list:
    """
    This function returns a list containing indexes of the starting point where the pattern is present as a substring
    of the genome with at most n mismatch
    Param:
    pattern: The pattern to find in the genome provided
    genome: The genome n: maximum
    number of mismatch allowed Returns: list(list): A list containing the index of the starting positions of the
    patterns in the genome
    """
    output: list = []
    k = len(kmer_pattern)
    gl = len(sequence) - k
    for i in range(gl):
        k_mer = sequence[i: i + k]
        """if this is an issue, try to find a better way to take care of cases where the length of the remaining 
        string is less than the length of the pattern """
        hd = hamming_distance(kmer_pattern, k_mer)
        if hd <= int(tolerance):
            output.append(i)
    return output


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("[Usage]: python approx_pattern_matching.py file")
        quit()
    file_input = sys.argv[1]
    pattern = ""
    genome = ""
    n = 0

    if os.path.isfile(file_input) and os.path.exists(file_input):
        with open(file_input) as f:
            pattern = f.readline()
            genome = f.readline()
            n = f.readline()
    else:
        print(f"File {file_input} does not exist")
        quit()
    print(n)
    indexes = approximate_pattern_matching(genome, pattern, n)
    print(f"starting indexes for matching pattern is {str(indexes).replace(',', ' ')}")

