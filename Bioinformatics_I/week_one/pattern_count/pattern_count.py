import argparse
import getopt
import sys, os
from typing import List


class PatternCount:
    def __init__(self, genome: str, pattern: str, pattern_length: int):

        if os.path.isfile(genome):
            self.genome = open(genome).read().strip()
        else:
            self.genome = genome

        if os.path.isfile(pattern):
            self.pattern = open(pattern).read().strip()
        else:
            self.pattern = pattern

        self.pattern_length = pattern_length

    # count counts how many times the pattern appears in the genome
    def count(self) -> int:
        # the index to stop the loop at.
        end_index = len(self.genome) - len(self.pattern)
        count = 0
        for index in range(0, end_index):
            if self.genome[index:index + len(self.pattern)] == self.pattern:
                count += 1

        return count

    # frequent returns a list of the k-mers that occurs more frequently
    def frequent(self) -> List[str]:
        end_index = len(self.genome) - self.pattern_length
        pattern_map = {}  # creates an empty dictionary

        for index in range(0, end_index):
            temp_pattern = self.genome[index:index + self.pattern_length]
            if temp_pattern in pattern_map.keys():
                pattern_map[temp_pattern] += 1
            else:
                pattern_map[temp_pattern] = 1

        max_pattern = [key for key, value in pattern_map.items() if value == max(pattern_map.values())]
        print(pattern_map)
        print(max_pattern)

        return max_pattern


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("[Usage]: python patter_count.py genome [file|text] pattern [file|text]")
        sys.exit()

    parser = argparse.ArgumentParser(
        description="[Usage]: python patter_count.py -g [file|text] -p [file|text] -k [int]")
    parser.add_argument("-g", "--genome", help="the genome either as a file or text")
    parser.add_argument("-p", "--pattern", help="the patter to search for (optional)")
    parser.add_argument("-k", "--pattern_length", help="the pattern length if you are checking for frequency")

    args = parser.parse_args()

    input_genome = input_pattern = pattern_length = ""

    if args.genome:
        input_genome = args.genome
    if args.pattern:
        input_pattern = args.pattern
    if args.pattern_length:
        pattern_length = args.pattern_length

    if input_pattern == "" and pattern_length == "":
        print("one of pattern_length or pattern_count must be provided")
        sys.exit()

    pc = PatternCount(input_genome, input_pattern, int(pattern_length))
    print(pc.frequent())
