""" Pattern count program

This module allows the user to determine the amount of times a pattern occurs in a genomic sequence
"""

from os import sys
def pattern_count(genome: str, pattern: str) -> int:
    """counts the amount of times a pattern occurs in a genomic sequence"""
    count: int = 0 # This represents the amount of time the pattern occurs in the sequence
    length: int = len(genome) - len(pattern) + 1 # Helps determine how many times to move forward
        # We have to add one to account for python's zero index
    for i in range(length):
        if genome[i:i+(len(pattern))] == pattern:
            count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("[Usage]: python pattern_count.py genome pattern")
        sys.exit()
    genome = sys.argv[1]
    pattern = sys.argv[2]

    print(f"Genome is {genome}")
    print(f"Pattern is {pattern}")

    print(f"The pattern {pattern} occurs {pattern_count(genome, pattern)} times in the genome provided")
