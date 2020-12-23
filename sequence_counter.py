def sequenceCounter(pattern: str, key: str) -> int:
    """
        counts the occurence of a particular key in a given genomic pattern
    """
    sum = 0
    print(len(pattern))
    for i in range(len(pattern)):
        if pattern[i:i+len(key)] == key:
            sum += 1

    return sum


def frequentWords(pattern: str, k : int) -> dict:
    """
        returns the most frequent k-mers in a genomic pattern
    """
    res = {}
    frequent = []
    for i in range(0 ,len(pattern)):
        key = pattern[i:i+k]
        if key in res:
            res[key] += 1
        else:
            res[key] = 1
    # get the highest occurence in the pattern
    high = max(res.values())
    for i in res.keys():
        if res[i] == high:
            frequent.append(i)

    output = ' '.join(frequent)
    return output



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
