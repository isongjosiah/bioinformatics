from approx_pattern_matching import approximate_pattern_matching
import sys


def approximate_pattern_count(genome: str, pattern: str, n: int) -> int:
    """
    approximate_pattern_counts counts the number of occurrence of the patter in the genome with a maximum mismatch of n
    Params:
    genome(str): text that is being scanned
    patter(str): pattern that is scanned for
    n: maximum number of mismatch allowed in pattern
    Returns
    frequency(int): the number of times a patter with a maximum allowed mismatch of n is found in the genome
    """

    print("genome is: ", genome)
    print("pattern is: ", pattern)
    temp_list = approximate_pattern_matching(genome, pattern, n)
    return len(temp_list)


genome = sys.argv[1]
pattern = sys.argv[2]
n = sys.argv[3]
count = approximate_pattern_count(genome, pattern, 2)
print("count: ", count)
