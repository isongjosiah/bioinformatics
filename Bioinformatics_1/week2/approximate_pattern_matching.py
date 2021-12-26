
from hamming_distance import hamming_distance


def approximate_pattern_matching(genome: str, pattern: str, n: int) -> list:
    """
    This function returns a list containing indexes of the starting point where the pattern is present as a substring of the genome with at most n mismatch
    Param: 
    pattern: The pattern to find in the genome
    genome: The genome
    n: maximum number of mismatch allowed
    Returns:
    list(list): A list containing the index of the starting positions of the patterns in the genome
    """
    output: list = []
    k = len(pattern)
    for i in range(len(genome)):
        k_mer = genome[i: i+k]
        """ if this is an issue, try to find a better way to take care of cases where the length of the remaining string is less than the length of the pattern"""
        if (len(k_mer) < k):
            break
        hd = hamming_distance(pattern, k_mer)
        if hd <= n:
            output.append(str(i))
    return(output)




#y = approximate_pattern_matching(genome, pattern, 6)
#print(" ".join(y))
