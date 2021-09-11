import sys

def sequenceCounter(pattern: str, key: str) -> int:
    """
        counts the occurence of a particular key in a given genomic pattern
    """

    print("genome: ", pattern)
    print("pattern: ", key)
    sum = 0
    print(len(pattern))
    for i in range(len(pattern)):
        if pattern[i:i+len(key)] == key:
            sum += 1

    print(sum)

genome = sys.argv[1]
pattern = sys.argv[2]

sequenceCounter(genome, pattern)
