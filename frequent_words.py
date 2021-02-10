def frequentWords(pattern: str, k : int, limit=0) -> dict:
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
    if limit == 0:
        limit = max(res.values())
    for i in res.keys():
        if res[i] >= limit:
            frequent.append(i)

    output = ' '.join(frequent)
    return output
