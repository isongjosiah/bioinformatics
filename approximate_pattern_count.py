from approximate_pattern_matching import approximate_pattern_matching


def approximate_pattern_count(genome: str, pattern: str, n: int) -> int:
    """
    approximate_pattern_counts counts the number of ooccurence of the patter in the genome with a maximum mismatch of n
    Params:
    genome(str): text that is being scanned
    patter(str): paattern that is scanned for
    n: maximum number of mismatch allowed in pattern
    Returns 
    frequency(int): the number of times a patter with an maximum allowed mismatch of n is found in the genome
    """
    list = approximate_pattern_matching(genome, pattern, n)
    return len(list)


genome = "TCTTGAATTGGGGGCAGGCGACTTATACCGGGCAGATCCGGTAATAAGGGGTAACACTATCGACTACTATGTCGGATGGTGTCGTCGGAAGGGGCTCCCGCCATCGATATGTCAGGCTAGCCCTAAGGCGAAGATGGGAGGGGTTTTACTCTGAAAGCCAAGACTTCTCCATACCGCTAAATACGCCGGTTGCCGCTAGTAGCTTAGGTGTGCCGTGCAGGTGAGTCCAGCGGCGATTTTGAATATATAGTACGACAGGCGCTGGGTTGTTGCTCTCCTGGTACAACGTAAGTGCTAGTGCGCTATCCAGTGTACCACTGACAAAAAGTGCCCACATTACAAGATGGGAGGTGATGGACTCGCGGTAAAGA "
pattern = "CTAGCCC"

count = approximate_pattern_count(genome, pattern, 3)
print(count)
