from hamming_distance import hamming_distance


def frequent_words_with_mismatch(genome: str, k: int, n: int) -> list:
    """
    This functioin just like frequent word returns a list of the most frequent words the twist is that this one also allows for up to n number of base mismatch
    Params:
    genome(str)
    k(int): length of pattrns to search for
    n(int): maximum number of mismatch allowed in pattern
    """
    patterns: list = []
    freq_map: dict = {}
    length = len(genome)

    for i in range(length-k):
        patterns = patterns.append(genome[i:i+k])


def neighbors(pattern: str, d: int) -> list:
    """
    This generates the d-neighborhood Neighbors(Pattern, d)
    """
    neighborhood: set = set()
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ["A", "C", "G", "T"]

    first_symbol = pattern[0]
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for base in "ACGT":
                text = base + text
                neighborhood.add(text)
        else:
            text = first_symbol + text
            neighborhood.add(text)
    print(neighborhood)
    return neighborhood


print(" ".join(neighbors("ACG", 1)))
