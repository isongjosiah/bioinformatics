def computing_frequencies(text:str, k:int)-> list:



def pattern_to_number(pattern:str)-> int:
    """
        pattern_to_number returns a index representing a the pattern
    """

    pre = ""
    # convert from base 4 to 10
    for i in pattrn:
        pre += ref[i]
    out = int(pre, 4)
    return out


def number_to_pattern(number: int, k: int)-> int:
    """
        number_to_pattern converts a decimal number to a k-mer
    """
    ref = {"A":0, "C":1, "T":2, "G":3}
    # convert the number from base 10 to 4
