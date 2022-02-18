import os

from approximate_pattern_matching import approximate_pattern_matching
import sys


def approximate_pattern_count(genome: str, pattern: str, n: int) -> int:
    """
    approximate_pattern_counts counts the number of occurrence of the pattern in the genome with a maximum mismatch of n
    Params:
    genome(str): text that is being scanned
    patter(str): pattern that is scanned for
    n: maximum number of mismatch allowed in pattern
    Returns
    frequency(int): the number of times a patter with a maximum allowed mismatch of n is found in the genome
    """
    temp_list = approximate_pattern_matching(genome, pattern, n)
    return len(temp_list)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("[Usage]: python approximate_pattern_count.py file")
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

    pattern = pattern.strip()
    genome = genome.strip()

    if len(genome) > len(pattern):
        count = approximate_pattern_count(genome, pattern, n)
    else:
        count = approximate_pattern_count(pattern, genome, n)
    print(f"approximate patter count is {count}")