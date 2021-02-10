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
