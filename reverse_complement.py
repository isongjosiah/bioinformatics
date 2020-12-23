def reverse_complement(pattern: str) -> str:
    """
        returns the reversse complement of a given DNA strand
    """
    ref = {"A":"T", "T":"A", "C":"G", "G":"C"}
    complement = ""
    for i in pattern:
        complement += ref[i]
    print(complement)
    reversed_complement = complement[::-1]
    return reversed_complement
